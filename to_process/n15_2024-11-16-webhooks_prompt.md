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
date: 2024-11-16 17:54
title: webhooks
tags:
  - webhooks
  - backend
  - devops
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
# webhooks
`$= dv.current().file.tags.join(" ")`

- [Backend](/uncategorized/backend/). devops 
- webhook vs API
	- devolución de llamada HTTP o una petición HTTP POST generada por la notificación de un evento
	- api mas control menos eventos
	- server inicia la data, id de eventos mas control
	- update automatico
	- notificaciones instantaneas vs cambios precios, stock, reembolsoos
- Acerca de webhooks - Documentación de GitHub
- Webhook- ¿Qué es y por qué lo necesitas- - Mailjet
- HTTP Post, endpoints
- triggers, eventos en tiempo real
- ejemplos
	- automatizaciones en CRM, realizar pedidos, generar presentaciones, notificar eventos
	- usar en wordpress [PHP](/backend/php/)
	- automatizar envio de emails, con button en notion, filtro de enviados
	- avisos slack, panel de control, correos, mensajes de wasap, historial..
- [Mailjet](https://www.mailjet.com/es/) 
- [ClickUp™ | One app to replace them all](https://clickup.com/lp?utm_source=google&utm_medium=cpc&utm_campaign=gs_cpc_emea-eea_nnc_brand_trial_all-devices_troas_lp_x_all-departments_x_brand&utm_content=all-countries_kw-target_text_all-industries_all-features_all-use-cases_clickup_broad&utm_term=b_clickup&utm_creative=651395804534_BrandChampion-03072023_rsa&utm_custom1=&utm_custom2=&gad_source=1&gclid=Cj0KCQjwmt24BhDPARIsAJFYKk2P-RYa9LfXR5gzzuDpqgN-df0YpIuHC5gRLZ_dzeTB5fIYEtUlHjcaAj-mEALw_wcB) 
- [Home | Make](https://www.make.com/en?utm_campaign=gg-dg-eur-demandgen-search-brand&utm_source=google&utm_medium=cpc&utm_content=make&utm_term=make%20integrations&gad_source=1&gclid=Cj0KCQjwmt24BhDPARIsAJFYKk2GjjZstPgMdhnD1gjBgF-X9pv8_hcfh4lfn15Sy14dk3sWhNDHjQUaAlFrEALw_wcB) 
- [Cómo Conectar Cualquier Aplicación con Webhooks 🪝 - YouTube](https://youtu.be/oPX-rPa3DuY) 
- [How WebHook works | System Design - YouTube](https://youtu.be/oQaJn6RdA3g)
	- polling vs **websockets** 
	- webhook; push, dirigido por eventos
	- Http; poll, dirigido por tiempo
	- event driven programing
	- notifications, fetch obj, client - back api - url
	- http post
	- commets, orders
	- XML JSON
	- notificaciones de SMS Computer Science
		- cliente escucha al webhook por la url
- [TODO sobre los WEBHOOKS de la API WhatsApp - YouTube](https://youtu.be/41_4Q5NApTw) 
	- api de wasap, ngrock proxy,
	- configurar webhook, 
	- template para inciar mensaje al cliente
	- [Wasapi | Gestiona, Vende y Automatiza en WhatsApp con IA](https://www.wasapi.io/) 
- open source
	- [Powerful Workflow Automation Software & Tools - n8n](https://n8n.io/) 
	- [GitHub - n8n-io/n8n: Free and source-available fair-code licensed workflow automation tool. Easily automate tasks across different services.](https://github.com/n8n-io/n8n)
	- router, filtros
- webhook con net
	- [What Exactly is a Webhook & How Do You Build One with .NET? 🚀 - YouTube](https://youtu.be/wtpAA-mkOlA) 