#!/usr/bin/env python3
import re
import json
import uuid
import hashlib
from pathlib import Path
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.exceptions import BadRequest
import threading
import time

# Configuración global
BASE_DIR = Path(__file__).resolve().parent
CONFIG = {
    "source_dir": BASE_DIR / "public_notes",
    "process_dir": BASE_DIR / "to_process", 
    "output_dir": BASE_DIR / "processed_notes",
    "status_file": BASE_DIR / "notes_status.json",
    "port": 5500,
    "prompt_template": """---
Actúa como un experto en transformación de notas técnicas a artículos de blog. 

Sigue estas reglas Mantén el tono técnico pero accesible. Sigue estrictamente las reglas: 

1. **Conservación Estructural**: 
    - Mantener TODOS los enlaces [[internos]] y [externos](url) exactamente como están 
    - Preservar los bloques de código y fragmentos técnicos sin modificación 
    - Convertir listas anidadas en jerarquía de headings (H2 para ítems principales, H3 para sub-ítems) 

2. **Expansión de Contenido**:
	- Introducción clara (¿Qué es? ¿Para qué sirve?)
    - Secciones técnicas organizadas
    - Explicaciones prácticas con ejemplos
    - Conclusión con recursos adicionales (ÚNICAMENTE usando enlaces ya presentes en el contenido original)
     - Para cada ítem de lista técnica, añadir:
	     * 1 párrafo explicativo (50-80 palabras)
	     * 1 ejemplo práctico cuando sea aplicable
	     * Consideraciones de uso profesional

3. **Formato de Salida**:
  - No generes el bloque YAML superior 
   - Usar Markdown 
   - Secciones claras con introducción y conclusión
   - Conclusión y Recursos Adicionales con solo [enlaces externos](url) existentes

4. **Importante**:  
    - NO añadas ningún texto introductorio o final fuera del artículo (como "Aquí tienes el artículo..." o "A continuación...")  
    - La respuesta debe comenzar directamente con el contenido transformado en formato Markdown
--- CONTENIDO ORIGINAL ---
"""
}

class NotesManager:
    def __init__(self):
        print(f"BASE_DIR: {BASE_DIR}")
        print(f"Source dir: {CONFIG['source_dir']}")
        self.ensure_dirs()
        self.status = self.load_status()
        self._file_hashes = {}
        self._monitoring = False

    def ensure_dirs(self):
        for dir in [CONFIG['source_dir'], CONFIG['process_dir'], CONFIG['output_dir']]:
            try:
                dir.mkdir(exist_ok=True, parents=True)
                print(f"Directory ensured: {dir}")
            except Exception as e:
                print(f"Error creating directory {dir}: {e}")
                raise

    def load_status(self):
        if CONFIG['status_file'].exists():
            try:
                with open(CONFIG['status_file'], 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error loading status file: {e}")
                return {"notes": {}, "next_id": 1}
        return {"notes": {}, "next_id": 1}

    def save_status(self):
        try:
            with open(CONFIG['status_file'], 'w', encoding='utf-8') as f:
                json.dump(self.status, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving status: {e}")

    @staticmethod
    def get_file_hash(path: Path) -> str:
        try:
            content = path.read_bytes()
            return hashlib.sha256(content).hexdigest()
        except Exception as e:
            print(f"Error getting hash for {path}: {e}")
            return ""

    def start_monitoring(self):
        """Inicia el monitoreo de archivos en un hilo separado"""
        if not self._monitoring:
            self._monitoring = True
            monitor_thread = threading.Thread(target=self._monitor_files, daemon=True)
            monitor_thread.start()
            print("File monitoring started")

    def _monitor_files(self):
        """Monitorea cambios en los archivos de origen"""
        while self._monitoring:
            try:
                self.check_for_changes()
                time.sleep(2)  # Verificar cada 2 segundos
            except Exception as e:
                print(f"Error in file monitoring: {e}")
                time.sleep(5)

    def check_for_changes(self):
        """Verifica cambios en los archivos sin regenerar todo"""
        changes_detected = False
        
        for note_file in CONFIG['source_dir'].glob("*.md"):
            current_hash = self.get_file_hash(note_file)
            file_key = note_file.stem
            
            # Verificar si el hash cambió
            if file_key in self._file_hashes:
                if self._file_hashes[file_key] != current_hash:
                    print(f"Change detected in {file_key}")
                    self._update_note_from_file_change(note_file, current_hash)
                    changes_detected = True
            
            self._file_hashes[file_key] = current_hash
        
        if changes_detected:
            self.save_status()

    def _update_note_from_file_change(self, note_file: Path, new_hash: str):
        """Actualiza una nota específica cuando se detecta un cambio"""
        file_stem = note_file.stem
        
        # Buscar la nota existente
        note_id = None
        for nid, info in self.status["notes"].items():
            if info["original_name"] == file_stem:
                note_id = nid
                break
        
        if note_id:
            note_info = self.status["notes"][note_id]
            previous_status = note_info["status"]
            
            # Determinar el nuevo estado basado en el anterior
            if previous_status in ["completed", "reprocessed"]:
                new_status = "modified_external"
            else:
                new_status = "pending"
            
            # Actualizar la información
            note_info.update({
                "status": new_status,
                "last_checked": datetime.now().isoformat(),
                "original_hash": new_hash,
                "modification_source": "source_file",
                "previous_status": previous_status
            })
            
            # Regenerar archivo de prompt
            self._regenerate_prompt_file(note_id, note_info)
            
            print(f"Updated note {note_id} ({file_stem}) from {previous_status} to {new_status}")

    def generate_notes(self):
        """Genera y actualiza el estado de todas las notas"""
        for note in CONFIG['source_dir'].glob("*.md"):
            current_hash = self.get_file_hash(note)
            matched = False
            
            for note_id, info in self.status["notes"].items():
                if info["original_name"] == note.stem:
                    matched = True
                    if current_hash != info.get("original_hash"):
                        # Cambiar el estado según el origen de la modificación
                        if info["status"] in ["completed", "reprocessed"]:
                            new_status = "modified_external"
                            print(f"Nota modificada detectada: {note.stem} (Estado anterior: {info['status']})")
                            info["status"] = new_status
                            info["modification_source"] = "source_file"
                        info["last_checked"] = datetime.now().isoformat()
                        info["original_hash"] = current_hash
                    break
            
            # Si no estaba registrada antes, es una nota nueva
            if not matched:
                note_id = f"n{self.status['next_id']}"
                self.status['next_id'] += 1
                status = "pending"
            else:
                # Reusar el ID que ya tenía
                status = self.status["notes"][note_id]["status"]
            
            # Reescribir to_process si es necesario
            if status in ("edited", "pending", "modified_external") or not matched:
                prompt_note = CONFIG['process_dir'] / f"{note_id}_{note.stem}_prompt.md"
                content = f"{CONFIG['prompt_template']}\n{note.read_text(encoding='utf-8')}"
                prompt_note.write_text(content, encoding='utf-8')
                
                if not matched:
                    self.status['notes'][note_id] = {
                        "original_name": note.stem,
                        "prompt_file": str(prompt_note),
                        "content": content,
                        "status": status,
                        "created_at": datetime.now().isoformat(),
                        "original_hash": current_hash,
                        "last_checked": datetime.now().isoformat()
                    }
                else:
                    self.status['notes'][note_id].update({
                        "prompt_file": str(prompt_note),
                        "content": content,
                        "last_checked": datetime.now().isoformat()
                    })
        
        self.save_status()
        return self.status

    def process_response(self, note_id, content):
        try:
            if not note_id or not content:
                raise ValueError("Datos incompletos")
                
            if note_id not in self.status['notes']:
                raise ValueError("ID de nota no encontrado")

            note_info = self.status['notes'][note_id]
            original_name = note_info['original_name']
            
            # Validar contenido original
            original_path = CONFIG['source_dir'] / f"{original_name}.md"
            if not original_path.exists():
                raise FileNotFoundError(f"Archivo original no encontrado: {original_path}")

            original_content = original_path.read_text(encoding='utf-8')
            yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', original_content, re.DOTALL)
            yaml_content = yaml_match.group(0) if yaml_match else "---\n---\n"
            
            # Crear directorio si no existe
            CONFIG['output_dir'].mkdir(exist_ok=True)
            
            # Escribir archivo procesado
            processed_content = f"{yaml_content}\n{content.strip()}"
            output_file = CONFIG['output_dir'] / f"{original_name}.md"
            output_file.write_text(processed_content, encoding='utf-8')
            
            # Determinar el nuevo estado basado en el estado anterior
            previous_status = note_info.get('status', 'pending')
            new_status = 'reprocessed' if previous_status in ['completed', 'modified_external', 'modified_internal'] else 'completed'
            
            # Actualizar estado con información de reprocesamiento
            note_info.update({
                'status': new_status,
                'processed_file': str(output_file),
                'processed_at': datetime.now().isoformat(),
                'last_modified': datetime.now().isoformat(),
                'modification_source': 'manual_reprocess' if previous_status in ['completed', 'modified_external'] else 'initial_process',
                'content_length': len(content),
                'previous_status': previous_status
            })
            self.save_status()
            
            return {
                'success': True,
                'output_file': str(output_file),
                'original_name': original_name,
                'processed_at': note_info['processed_at'],
                'new_status': new_status
            }
            
        except Exception as e:
            print(f"Error processing response: {e}")
            return {
                'success': False,
                'error': str(e),
                'note_id': note_id
            }

    def update_note_status(self, note_id, status):
        if note_id in self.status['notes']:
            note_info = self.status['notes'][note_id]
            
            # Guardar el estado anterior con timestamp
            previous_status = note_info.get('status')
            note_info['status_history'] = note_info.get('status_history', [])
            note_info['status_history'].append({
                'status': previous_status,
                'changed_at': datetime.now().isoformat()
            })
            
            # Actualizar el estado
            note_info['status'] = status
            note_info['last_modified'] = datetime.now().isoformat()
            
            # Manejar casos especiales
            if status == 'pending' and previous_status in ['completed', 'reprocessed', 'modified_external']:
                note_info['reprocess_count'] = note_info.get('reprocess_count', 0) + 1
                note_info['last_reprocess_request'] = datetime.now().isoformat()
                note_info['modification_source'] = 'manual_reprocess'
                # Regenerar el archivo en to_process
                self._regenerate_prompt_file(note_id, note_info)
            
            self.save_status()
            return True
        return False

    def _regenerate_prompt_file(self, note_id, note_info):
        """Regenera el archivo en to_process para notas reprocesadas"""
        try:
            original_path = CONFIG['source_dir'] / f"{note_info['original_name']}.md"
            if original_path.exists():
                prompt_note = CONFIG['process_dir'] / f"{note_id}_{note_info['original_name']}_prompt.md"
                content = f"{CONFIG['prompt_template']}\n{original_path.read_text(encoding='utf-8')}"
                prompt_note.write_text(content, encoding='utf-8')
                note_info['prompt_file'] = str(prompt_note)
                note_info['content'] = content
        except Exception as e:
            print(f"Error regenerating prompt file: {e}")

# Crear la aplicación Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Instancia global del manager
notes_manager = NotesManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_notes')
def get_notes():
    try:
        # Regenerar notas para capturar cambios
        notes_manager.generate_notes()
        return jsonify(notes_manager.status)
    except Exception as e:
        print(f"Error in get_notes: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/update_status', methods=['POST'])
def update_status():
    try:
        data = request.get_json()
        if not data:
            raise BadRequest("No JSON data provided")
        
        note_id = data.get('note_id')
        status = data.get('status')
        
        if not note_id or not status:
            raise BadRequest("Missing note_id or status")
        
        success = notes_manager.update_note_status(note_id, status)
        
        return jsonify({
            'success': success,
            'note_id': note_id,
            'new_status': status
        })
        
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f"Error in update_status: {e}")
        return jsonify({'error': 'Server error', 'details': str(e)}), 500

@app.route('/process_response', methods=['POST'])
def process_response():
    try:
        data = request.get_json()
        if not data:
            raise BadRequest("No JSON data provided")
        
        note_id = data.get('note_id')
        content = data.get('content')
        
        if not note_id or not content:
            raise BadRequest("Missing note_id or content")
        
        result = notes_manager.process_response(note_id, content)
        
        status_code = 200 if result.get('success') else 400
        return jsonify(result), status_code
        
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f"Error in process_response: {e}")
        return jsonify({'error': 'Server error', 'details': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == "__main__":
    # Inicializar el manager y generar notas
    notes_manager.generate_notes()
    
    # Iniciar monitoreo de archivos
    notes_manager.start_monitoring()
    
    print(f"Servidor Flask ejecutándose en http://localhost:{CONFIG['port']}")
    print(f"Interfaz disponible en: http://localhost:{CONFIG['port']}")
    
    # Ejecutar la aplicación Flask
    app.run(
        host='0.0.0.0',
        port=CONFIG['port'],
        debug=True,
        use_reloader=False  # Desactivar reloader para evitar conflictos con el monitoreo
    )
