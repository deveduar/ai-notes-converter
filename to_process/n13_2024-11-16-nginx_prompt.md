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
date: 2024-11-16 17:03
title: nginx
tags:
  - nginx
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
# nginx 
`$= dv.current().file.tags.join(" ")`

- devops
- [Backend](/uncategorized/backend/)
- Redes
- [apache](/uncategorized/apache/) 
- nginx-features
- NGINX- ¿qué es y en qué se distingue de Apache-
- Beginner’s Guide 
- [int-nginx.code-workspace](file:///D:%5CDocs%20Hp%5CCode-projects%5Cint-nginx.code-workspace) 💻
- conceptos
	- virtual hosts
	- sites aviable, json obj
	- reverse proxy
	- SSL
	- buffer
	- [nginx](https://nginx.org/en/) 
	- 
- [Enrutamiento y Balanceo de carga con NGINX para tus aplicaciones de Microservicios - YouTube](https://youtu.be/o7DSHPji1m0) 
	- critero de peticiones
	- balance de carga, cookies, hash, servicio con estado
	- router, url, regex
	- [microservicios](/backend/microservicios/)
	- service workers
	- balanceo de carga vs router
	- proxy
	- round robin
	- mapeo de files
- instalacion 
	- docker
	- [hub.docker.com/\_/nginx](https://hub.docker.com/_/nginx)  

- **nginx proxy manager** 
	- [Nginx Proxy Manager](https://nginxproxymanager.com/)
	- [Cómo crear un Servidor Web Compartido con Docker y Nginx Proxy Manager (NPM) 🚀 - YouTube](https://youtu.be/WCSdh37Z6Wk)
	- proxy 
	- devops
	- docker 
	- [nginx](/backend/nginx/)
	- Traefik 
	- **reverse proxy** 
		- proxy host by ip
	- redirigir trafico entre contenedores **DNS**
	- **whitelist de ips**
	- orquestar contenedores con doker swarm vs Kubernetes
		- pabperezadocs at main · pabperezapabpereza-113.Docker_swarm
	- network list, create
	- crear proxy host
	- redireccion en file host, 
		- registro de dns de tipo a
		- o falsea en producion usar dominio
	- manejar certificados SSL
	- quitar puertos del docker compose
		- crear puertos para el proxy
- servidor web como servicio?
- conf files
	- enrutamiento de ips, hosts, 
	- virtual hosts, redirecciones
- subdominio en duckdns DNS
	- [Duck DNS](https://www.duckdns.org/) 
	- router con loopback
	- vpn
- api getaway
	- proxy
	- grafana
-  nginx con nodejs
	- [Full NGINX Tutorial - Demo Project with Node.js, Docker - YouTube](https://youtu.be/q8OleYuqntY) 
	- conceptos
		- un entry point
		- catching
		- security
		- un entrypoint
		- compresion. segmentacion, chunks
		- nginx conf
		- redirect http to https
		- load balancing vs  proxy 
			- ej: instacias de la app, proxy a grupo del server, 
			- **round robin** 
			- enrutar servicios
			- control de carga en server y cluster en cloud Kubernetes
		- cache
	- replicas de node js en el docker yml con services, puertos
	- vs [apache](/uncategorized/apache/)
	- conf inicial
		- [nginx/conf/nginx.conf at master · nginx/nginx · GitHub](https://github.com/nginx/nginx/blob/master/conf/nginx.conf) 
		- [Alphabetical index of directives](https://nginx.org/en/docs/dirindex.html) 
		- **reverse proxy**
			- workers, events, 
			- http (context)
				- server, location, proxy_pass , (entry point) 
				- upstreams, cluster
		- domain y subdomain
			- routing, headers
			- ``proxy_set_header Host $Host``
			- enviar peticiones con ip a los bakends
			- `proxy_set_header X-Real-IP $remote_addr`
		-  file types de la response header content-type
			- MIME types
			- renderizado en el cliente
			- `include mime.types;`
		- en cluster `leadt__conn` para load balancing
		- directives vs context
		- `nginx -V` ver logs
		- **SSL**  vs TSL confs
			- `openssl`
			- key par, .crt y .key
			- `listen 433 ssl;` 
			- `ssl_certificate_key`
			- `ssl_certificate`
		- cargaar conf en reinicio
			- `nginx -s reload` 
			- `nginx -s stop` 
			- `ps aux | grep nginx`
		- redireccion a https endpoint
			- port 301
			- nuevo server en conf con location
				- `listen 80`
				- `return 301 https//$host$request_uri`
- en linux
	- [Despliegue de páginas webs usando Docker + Nginx + Ubuntu - YouTube](https://youtu.be/HKsTlmZpZMA) 
		- Linux 
		- docker
			- `-v` volumes, mapear carpeta al contenedor
	- [Servidor Web con Docker - NGINX 🐳 #3 - YouTube](https://youtu.be/xZIUAL7YYs8) 
- imagen de docker
	- [GitHub - nginxinc/docker-nginx: Official NGINX Dockerfiles](https://github.com/nginxinc/docker-nginx/tree/master) 
	- [hub.docker.com/\_/nginx](https://hub.docker.com/_/nginx) 
	- uso de templates para la conf
		- [hub.docker.com/\_/nginx](https://hub.docker.com/_/nginx)
	- copy en dockerfile vs templates para conf y uso de envfile
- [Nginx Mastery | Getting Started with Nginx | Docker | Docker Compose - YouTube](https://www.youtube.com/watch?v=7tGhir27ZJo&list=PLOLrQ9Pn6cawvMA5JjhzoQrnKbYGYQqx1) 
	- [GitHub - veryacademy/yt-nginx-mastery-series](https://github.com/veryacademy/yt-nginx-mastery-series) 
	- 
- 
## omnivore  nginx
```dataviewjs

const tagNames = ["nginx", "Nginx"]; 

let pagesWithTag = [];

// Filtrar y recopilar las páginas que tienen alguno de los tags especificados
dv.pages('"Omnivore"').forEach(page => {
    if (page.tags) {
        // Verificar si alguno de los tags especificados está en los tags de la página
        if (tagNames.some(tag => page.tags.includes(tag))) {
            pagesWithTag.push(page);
        }
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
