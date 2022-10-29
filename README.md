# website
Website de la comunidad Python La Paz
## Desarrollo
Para levantar en formato desarrollo
```sh
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build
```
## Producción
Archivos requeridos para el website en producción
```sh
cp backend.env website/.env
cp database.env database/.env
```
Configurar los archivos .env

Para levantar en produccion sin traefik
```sh
docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.prod.local.yml up -d
```
## Producción con Traefik
Para traefik copiar el archivo 
```sh
cp traefik.env .env
```
Configurar el archivo .env
Para levantar en produccion con traefik
```sh
docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.prod.traefik.yml up -d
```
 
Para levantar en produccion con traefik en servidores ARM 64 
```sh
docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.prod.traefik.yml -f docker-compose.prod.traefik.arm64.yml up -d
```


## Crear super usuario
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.prod.traefik.yml -f docker-compose.prod.traefik.arm64.yml exec app python manage.py createsuperuser
```