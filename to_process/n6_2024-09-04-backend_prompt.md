---
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

---
date: 2024-09-04 19:26
title: Backend
tags:
  - backend
  - api
keywords: 
source: 
status: 🚀
Parent: "[[Area-Prog]]"
cssclasses:
  - wide
public_note: true
public: true
category: uncategorized
categories:
  - uncategorized
---
gggggggggggggggggggggggg
gggggggggggggggggggggggggggggg































	- concurrencia. multihilos 
	- rutas, fetching, 
	- **Mixins** no JS
	- autenticacion
		- ciberseguridad
		- hashear passwords
			- bcryp
			- riesgo de trunkar
		- cache key
- procesamiento de datos
	- [Stream Processing](/backend/stream-processing/)
	- Casos de uso Event Sourcing
- arquitecturas web
	- [microservicios](/backend/microservicios/) 
	- [monorepo](/backend/monorepo/)
	- [gestor de colas](/backend/gestor-de-colas/)
- protocolos Comunicación
	- [websockets](/backend/websockets/) 
	- [webhooks](/backend/webhooks/) 
	- [web services](/backend/web-services/)
	- [api](/backend/api/)
- diseño de sistemas backend
	- Databases 
	- [CORS](/backend/cors/)
	- [server actions](/backend/server-actions/) 
	- [serverless](/backend/serverless/) 
	- [Runtime Management](/backend/runtime-management/)
	- escalabilidad
		- [Instance Scaling](/backend/instance-scaling/)
	- cache, particionar db sharding?, sql vs nosql, 
	- db master y slaves, replicar db
	- dns, peticiones de db, cdn para static files, latencia, 
	- way vs balancing
	- pasar id de sercretos a fun en runtime, reset del servicio
	- 





## omnivore backend
```dataviewjs
// Configuraciones
const tagName = "backend";

// Crear un array para almacenar las páginas que contienen el tag
let pagesWithTag = [];

// Filtrar y recopilar las páginas que tienen el tag
dv.pages('"Omnivore"').forEach(page => {
    if (page.tags && page.tags.includes(tagName)) {
        pagesWithTag.push(page);
    }
});

// Ordenar las páginas por 'date_saved' en orden descendente
pagesWithTag.sort((a, b) => {
    return b.date_saved.localeCompare(a.date_saved);
});

// Iterar sobre cada página filtrada y ordenada
for (const page of pagesWithTag) {
    // Mostrar el enlace a la página
    dv.el('p', page.file.link).addClass("page-link");
}

```


