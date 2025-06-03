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
date: 2024-11-07 03:13
title: nodejs
tags:
  - nodejs
  - express
  - backend
keywords: 
source: 
status: 📌
Parent: "[[Area-Prog]]"
cssclasses:
  - hide-embedded-header1
  - wide
categories:
  - Backend
public_note: true
public: true
category: Backend
---
# nodejs
b
bLint - Pluggable JavaScript Linter](https://eslint.org/docs/latest/use/getting-started) 
	- [What is Prettier? · Prettier](https://prettier.io/docs/en/) 
	- entorno de node y express, production?
		- [How I Set up Production Node.js Project (2024) - YouTube](https://youtu.be/GTDYsV5pyZU) 
		- node js template
		- [GitHub - alexrusin/node-template-2024](https://github.com/alexrusin/node-template-2024) 
		- [GitHub - alexrusin/node-template-2024 at add-sequelize](https://github.com/alexrusin/node-template-2024/tree/add-sequelize) 
	- github actions devops
		- workflows, trigger events, run actions (ej: tests)
		- **yml**
	- nodemon, 
	- env de ``AppDebug``
	- obj config con env, port, fun en obj
	- [ ] crear estructura de files, probat la env de debug, test de prueba
	- [ ] instalar db con docker, [hub.docker.com/\_/mysql](https://hub.docker.com/_/mysql) devops
	- [ ] usar **Sequelize** orm [TypeScript | Sequelize](https://sequelize.org/docs/v6/other-topics/typescript/) v6
		- [sequelize-typescript - npm](https://www.npmjs.com/package/sequelize-typescript) 
- [Curso Fundamentos de Node.js - jonmircha - YouTube](https://youtu.be/0f26_Enlv38)
	- [GitHub - jonmircha/youtube-nodejs: En este repositorio encontrarás los códigos del Curso de Node.js de @jonmircha](https://github.com/jonmircha/youtube-nodejs) 
	- Guía definitiva de Node.js- Introducción para desarrolladores - Evolve Academy
## buenas practicas react, js y nodejs
- env files y process ,env performace
	- conf js para envs y exportar obj
	- si usas un fun para cargar conf file que no haga process env en esa fun
		- no carge las env usar  ``process.loadEnvFile()`` y meter envs en const
- usar path relativos con `@`
- carga dinamica de componentes lazy, api de react?
- evitar ifs usando `onClose` en animaciones react  #react 
- promise.try para asegurar que es una promesa en un useEffect react #react
- `.?` optional changing
	- Optional chaining (.) - JavaScript  MDN-Optional_chaining 
	- evalua undefined en vez de error
- --what en vez de nodemon
## omnivore node js
```dataviewjs
// Configuraciones
const tagName = "nodejs";

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


