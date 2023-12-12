# PyEtiquetas
En este proyecto quiero lograr hacer etiquetas para mi mamá.

## Motivación
Mi mamá generalmente necesita imprimir etiquetas para su emprendimiento. Como no tenemos diseñador lo hacemos con Google slides y despues yo manualmente tengo que llenar una hoja con muchas copias de esa imagen en GIMP (photoshop de los pobres)

## Diseño de la solución

En algunas pegas atrás (Abaqus) usabamos reportlab para generar reportes en PDF para una app de Factsheets donde eran generados los reportes de manera automática en vez de tener que pedirle a un diseñador que recolecte la info y la muestre.

Reportlab tiene mucho tiempo de desarrollo y harta comunidad en stackoverflow, asi que me tiré a la aventura.

La solución actual es una Hoja de tamaño **legal** (Oficio) con una tabla de 5*2 para llenarse con  imágenes de **aspect ratio** 16:9

El script recibe por argumentos de línea de comandos una imagen y su salida es escribir un pdf con estas etiquetas.

## Instalación
Se debe tener instalado python3 y pip para poder empezar la instalación

Es recomendable tener Python 3.11 o superior.

Se instalan las dependencias con el siguiente comando
`pip3 install -r requirements.txt`

## Uso
para ejecutar la app solo basta con ejecutar lo siguiente en la línea de comandos 

`python3 etiquetas.py archivo1.jpg`
`python3 etiquetas.py archivo2.png`

el script sólo acepta imagenes jpg y png por ahora.

## Extras
agregué un `clean.sh` (para eliminar archivos pdf, png y jpg)

y agregué `batch.sh` para poder automatizar la ejecución 

Gracias por leer!

Saludos y bendiciones ``:)``