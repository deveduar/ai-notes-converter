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
date: 2024-11-07 03:11
title: nestjs
tags:
  - nestjs
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
# nestjs
`$= dv.current().file.tags.join(" ")`

- [Backend](/uncategorized/backend/)
- typescript
- 
- [Documentation | NestJS - A progressive Node.js framework](https://docs.nestjs.com/)
- [OpenAPI (Swagger) | NestJS - A progressive Node.js framework](https://docs.nestjs.com/openapi/introduction)
- intro
	- controllers, services
	- cli, test, 
	- mantenibilidad
	- providers, **entities**, **DTO**, Middleware,
	- pipes, guards, interceptors, custom decorators
	- basado en express o fastify
- [¿Qué es NESTJS? 🤔 Nest JS vs Express Parte 1 - YouTube](https://www.youtube.com/watch?v=lonpW-0EybY&list=PL_WGMLcL4jzWCFea1NUVOfaf4IqIMFN4P) 
	- controller: decoradores , get funs,
	- services: providers, constructor, db modelo
	- comprobar en postman
	- **resource** cli, ej: ``nest get resource name``
		- pasando string en controller se consigue acceso
		- crea metodos y clases y respuestas
	- **swagger**
	- OpenAPI (Swagger) - NestJS - A progressive Node.js framework
		- decorador `@ApiTags`
		- crear api tipada
		- 
- [ ] nest para back y next para front CRUD, Prisma
	- [Nextjs y Nestjs - Aplicación CRUD (con Typescript, Shadcn, prisma y más) - YouTube](https://www.youtube.com/watch?v=x2vY7gLzeCY) 
	- [Get started with Prisma | Prisma Documentation](https://www.prisma.io/docs/getting-started) 
- **estructura de proyectos**
	- [Si tuviera que empezar un nuevo proyecto de NestJS usaría esto! - YouTube](https://youtu.be/l--D8yslyUk) 
	- [ ] cambiar default template con el comando de crear app
	- mala estructura de ficheros no usa **solid** , 
	- test unitarios no separados y con conf en pkg json, usar convecion
	- no optimizado para produccion Kubernetes
	- usar compilador **SWC** en vez de tsc
	- **fastify** en vez de express, mas peticiones menos latencia
	- nivel de cobertura, **tests** unit vs  end to end, crear merge, hosting, **husky**,
	- niveles de log
	- **template personalizados**:
		- [GitHub - AlbertHernandez/nestjs-service-template: Template for new services based on NestJS with the Best Practices and Ready for Production](https://github.com/AlbertHernandez/nestjs-service-template) 
		- [GitHub - AlbertHernandez/express-typescript-service-template: Template for new services based on Express and Typescript with the Best Practices and Ready for Production](https://github.com/AlbertHernandez/express-typescript-service-template)
- [ ] sistema de pagos con arquitectura hexagonal, crear y listar pagos, sobrecomplicado, apps grandes
	- [GitHub - AlbertHernandez/nestjs-hexagonal-architecture-example: Example of how to create a NestJS service using hexagonal architecture](https://github.com/AlbertHernandez/nestjs-hexagonal-architecture-example) 
	- [Arquitectura Hexagonal en NestJS | Clean Architecture - YouTube](https://www.youtube.com/watch?v=4_4p5Ojs5XA) 
	- **arquitectura hexagonal**
		- dominio - app - infraestructura
		- capas internas no habla con capas externas
		- **puertos vs adapters** 
		- **unit of work**, operaciones atomicas para modificar pagos (ej: decoradores mongo prostgres)
			- decorador de transactonial, (uso en middleware) 👆
	- [ ] creacion de clases, interfaces, pagos y acceso a capas con caso de uso
	- **metodo para trabajar con primitivos en el domain** payment.entity
		- context/payments/domain, entidad payment.ts
		- definir **primitivos** con interfaz y construir en la clase de pagos los atributes, 
		- fun static para createPayment y fun para convertirlo ` id: this.attributes.id,`
		- *create()*
		- lib uuid
		- crear pagos con id de pago y customer y cantidad 
	- **clases abstractas** interfaz de pagos, contenedor de dependencias, gestion de db
		- payment.repository.ts
			- ``class PaymentRepository``	
		- excepciones
			- ``payment-not-found.exception.ts``
			- `export abstract class PaymentRepository {`
	- llamar a metodos del dominio en clase abstracta 
		- `export interface CreatePaymentDto {`
		- `export class CreatePaymentUseCase {`
			- promesa asyn, construtor private y readonly, construye el repositorio con los metodos abstractos 
				- `abstract save(payment: Payment): Promise<void>;`
				- `abstract findById(id: string): Promise<Payment | null>;`
			- funs *create*, *save*, 
			- devuelve obj con primitivos
	- **infrastructura**
		- servicio
		- caso de uso con interfaz **DTO** `payment_http-dto.ts`
		- uso de caso de pago file ts
		- **agnositico a la db**
		- llamar desde el repo
		- *@Controller*, *@Post*, *@Body*, *run()*
		- carpeta **shared** codigo compartido
			- crear inyectable parael ts de caso de uso
			- *@module* obj decorator con **providers**
			- implementacion del repository
		- [ ] endpointe de pagos
		- [ ] injectable personalizado
		- [ ] comprobar en postman el endpoint
		- capa infraestructura y capa http
		- controller vs dto
			- dto de capa http y aplicacion
		- pago a traves de repository si no existe excepcion

## omnivore nestjs
```dataviewjs
// Configuraciones
const tagName = "nestjs";

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

