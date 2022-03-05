## Requerimientos
1. Para el script, se utilizó a python como lenguaje de programación.
2. Descargar el ChromeDriver de la siguiente dirección: https://chromedriver.chromium.org/downloads

## Descripción
En este ejercicio técnico, se logra automatizar los procesos asociados al registro, login y agregado de 5 productos al carrito de compras de la página web https://staging-zapatoca.miaguila.com/registro/?hidecaptcha=true.

### Reistro y Login
Para la fase de registro y login, se deja en el script el payload de los datos que serán enviados al servidor.

### Agregar productos al carrito
En esta fase la estructura de los productos se asocia a una lista de webElemets que son visitados  uno a uno en orden para agregar al carrito el total de 5 productos.

### Detalles
Los elementos de la pagina, mayormante son ubicados en el DOM con xpath y cssSelector. Las esperas en mayor medida fueron explicitas a traves del metodo time.sleep()

### Ver Video

En el siguiente link se encuentra el video donde se evidencia el performance del script.
https://youtu.be/e-1Qk5QG5O8


