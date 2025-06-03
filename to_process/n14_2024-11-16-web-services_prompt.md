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
date: 2024-11-16 17:44
title: web services
tags:
  - webservices
  - devops
  - backend
  - microservicios
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
# web services
`$= dv.current().file.tags.join(" ")`

- [microservicios](/backend/microservicios/)
- [Backend](/uncategorized/backend/) 
- Data Science
- [Springboot](/backend/springboot/) 

- [JAX-WS](/backend/jax-ws/) 

- WSDL 
	- SOAP 
	- [WSDL - Documentación de IBM](https://www.ibm.com/docs/es/was-nd/8.5.5?topic=services-wsdl) 
	- Web Services Description Language
	- colecciones
	- metodos y parametros, tipos de datos, retorno
	- desciptor de servicio, cliente, consumer, servlet?
	- UDDI, servicios disponibles
	- definitions, types, message, portType, binding, servide
-  XML
	- tree, nodes
	- validaciones
		- xs element
	- [Python for Everybody - Web Services: XML Schema | Learn | freeCodeCamp.org](https://www.freecodecamp.org/learn/python-for-everybody/python-for-everybody/web-services-xml-schema) 
- conceptos
	- app de itercambio de data, API
	- GCP, AWS, Azure, Supabase, firebase, cloudflare, vercel
	- SOAP, Rest, HTTP, SML, URI, MIME
	- metodos restfull
	- provider, request, broker, 
	- comunicacion con protocolos estandar
	- tipos de errores
- videos
	- [▷ ¿Qué es un web service y cómo funciona? \[2024\]](https://www.crehana.com/blog/transformacion-digital/que-es-web-service/) 
	- [10/37 WEB SERVICES - ROLES Y PERFILES - YouTube](https://www.youtube.com/watch?v=nkBcqvpo7lE&list=PLBBoc2l3GGf3L3Oz_NtrYaP1pdTYOO_Iq) 
	- [Generalidades de los Web Services SOAP - YouTube](https://youtu.be/wT6w9BPapQg) java
		- interfaces, clases, constructor, endoints, ID @webservice 
		- protocolo direccion
	- [Ejemplo para el consumo de servicios web - YouTube](https://youtu.be/eSqW0XV257A) 
		- res y req SOAP
		- saapui soft, envio soap,
			- [Getting Started with API Testing | SoapUI](https://www.soapui.org/getting-started/) 
		- EJ: conectar con db sap, conexion a atraves de socket
		- ej: catastro
		- firma XML
		- ej egoi mail marketing
			- diccionarios soap, url
	- [Web Services. Introducción - YouTube](https://youtu.be/ViSDptzLrQY) 
	- [¿Qué diablos es un web service SOAP? | creación en C# .Net WCF - YouTube](https://youtu.be/ZeRiqOFXzZo) con net
	- [Como CREAR y CONSUMIR un WEB SERVICE en ASP.NET (C#) - YouTube](https://youtu.be/dl1xfgMxpbU) con net
	- [Node Js Express | web services | Creación api rest](https://luisjordan.net/node-js/web-services-con-node-js-express-creacion-de-api-rest/) 
- ejemplos
	- Una API REST que devuelve datos en formato JSON.
	- Un servicio SOAP que permite a sistemas bancarios intercambiar información.
	- Un GraphQL API para consultar múltiples datos en una sola petición.
