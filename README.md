# Gestor de Notas Gemini - Flask Version

## Características principales

- **Monitoreo en tiempo real**: Detecta automáticamente cambios en archivos sin reiniciar el servidor
- **Interfaz reactiva**: Actualización automática de la UI cada 3 segundos
- **Estados mejorados**: Mejor gestión de estados de notas (pendiente, copiado, procesado, modificado)
- **Arquitectura Flask**: Más mantenible y escalable que el servidor HTTP básico
- **Alpine.js**: Interfaz de usuario reactiva y moderna
- **CSS Modular**: Estilos organizados en módulos separados

## Instalación

1. Instalar dependencias:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. Ejecutar la aplicación:
\`\`\`bash
python app.py
\`\`\`

3. Abrir en el navegador:
\`\`\`
http://localhost:5500
\`\`\`

## Estructura de directorios

\`\`\`
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias Python
├── templates/
│   └── index.html        # Template HTML principal
├── static/
│   ├── css/             # Estilos CSS modulares
│   │   ├── base.css     # Variables y utilidades base
│   │   ├── components.css # Componentes reutilizables
│   │   ├── layout.css   # Layout y estructura
│   │   └── responsive.css # Responsive design
│   └── js/
│       └── app.js       # Lógica Alpine.js
├── public_notes/        # Notas originales (.md)
├── to_process/          # Notas preparadas para Gemini
├── processed_notes/     # Notas procesadas finales
└── notes_status.json    # Estado de las notas
\`\`\`

## Mejoras implementadas

### 1. Arquitectura modular
- **CSS separado**: Estilos organizados en módulos temáticos
- **Templates Flask**: HTML en archivos separados usando Jinja2
- **JavaScript modular**: Lógica Alpine.js en archivo independiente

### 2. Monitoreo de archivos en tiempo real
- Hilo separado que monitorea cambios cada 2 segundos
- Detección automática de modificaciones sin reiniciar
- Actualización inmediata del estado de las notas

### 3. Interfaz reactiva mejorada
- Auto-refresh cada 3 segundos en el frontend
- Preservación del estado de la UI durante actualizaciones
- Notificaciones en tiempo real de cambios
- Estados vacíos informativos
- Badges con contadores en las pestañas

### 4. Responsive design completo
- Diseño adaptable para móviles y tablets
- Navegación optimizada para pantallas pequeñas
- Soporte para modo landscape
- Estilos de impresión
- Soporte para preferencias de accesibilidad

### 5. Estados de nota mejorados
- `pending`: Nueva nota o lista para procesar
- `copied`: Copiada al portapapeles
- `completed`: Procesada exitosamente
- `reprocessed`: Reprocesada después de modificación
- `modified_external`: Modificada en archivo origen
- `modified_internal`: Modificada por reprocesamiento

## Uso

1. **Agregar notas**: Coloca archivos `.md` en `public_notes/`
2. **Copiar para Gemini**: Usa la pestaña "Notas para Copiar"
3. **Procesar respuestas**: Pega las respuestas de Gemini en "Procesar Respuestas"
4. **Revisar procesadas**: Ve el resultado en "Notas Procesadas"

## Ventajas sobre la versión anterior

- ✅ **Arquitectura limpia**: Separación clara de responsabilidades
- ✅ **CSS modular**: Estilos organizados y mantenibles
- ✅ **Templates Flask**: HTML separado del código Python
- ✅ **Sin reinicio**: Los cambios se detectan automáticamente
- ✅ **Tiempo real**: Interfaz se actualiza sin intervención manual
- ✅ **Responsive**: Funciona perfectamente en móviles
- ✅ **Accesible**: Soporte para preferencias de usuario
- ✅ **Escalable**: Fácil de extender y mantener
\`\`\`

Ahora tienes una aplicación Flask completamente modular con:

🎯 **Separación correcta de archivos**:
- `app.py` - Solo lógica de backend
- `templates/index.html` - Template HTML con Jinja2
- `static/css/` - CSS modular organizado por responsabilidades
- `static/js/app.js` - JavaScript Alpine.js

🎨 **CSS modular**:
- `base.css` - Variables CSS, reset y utilidades
- `components.css` - Componentes reutilizables (botones, badges, etc.)
- `layout.css` - Layout principal y estructura
- `responsive.css` - Responsive design completo

✨ **Características mejoradas**:
- Monitoreo en tiempo real sin reiniciar servidor
- Interfaz completamente responsive
- Estados vacíos informativos
- Badges con contadores en pestañas
- Mejor UX con notificaciones contextuales
- Soporte para accesibilidad y preferencias de usuario

La aplicación ahora es mucho más mantenible, escalable y profesional! 🚀
