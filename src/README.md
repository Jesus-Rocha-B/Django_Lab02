Laboratorio 02 - Catalogo Web de Ropa Streetwear (UrbanTrend)

Aplicacion web desarrollada en Django aplicando el patron de arquitectura Modelo-Vista-Plantilla (MVT), con gestion de datos en memoria RAM mediante listas de diccionarios.
Integrantes y Distribucion del Trabajo

    Erick Gamarra:

        Ejercicio 1: Investigacion y definicion de la problematica real.

        Ejercicio 2: Captura y redaccion de requisitos funcionales.

        Ejercicio 3: Diseno del modelo de datos y justificacion de campos.

        Ejercicio 4: Creacion y configuracion inicial de la aplicacion store en el proyecto.

        Ejercicio 9: Verificacion del flujo Request-Response, documentacion de pruebas y mejoras visuales en la interfaz.

        Ejercicio 10: Congelamiento de dependencias en requirements.txt y documentacion final.

    Jesus Rocha:

        Ejercicio 5: Implementacion de la estructura estatica en models.py y funciones auxiliares CRUD.

        Ejercicio 6: Implementacion del listado general (vista, URL y template prenda_list).

        Ejercicio 7: Diseno del formulario desacoplado en forms.py (PrendaForm).

        Ejercicio 8: Logica de creacion con metodo POST, validacion de datos y redireccion.

Problematica

En el sector de venta de ropa streetwear y marcas independientes, la mayoria de pequenos emprendedores comercializan sus productos mediante canales informales como historias temporales de WhatsApp o Instagram.

Esto genera problemas frecuentes:

    Las publicaciones desaparecen a las 24 horas, perdiendo visibilidad del catalogo.

    No existe un control visible del stock disponible en tiempo real.

    El vendedor debe responder repetidamente mensajes sobre tallas, precios y materiales.

UrbanTrend soluciona esto mediante una vitrina digital simple que centraliza el inventario, permitiendo consultar especificaciones de cada prenda, filtrar por categorias y registrar nuevos productos de forma rapida.
Requisitos Funcionales

    RF01: Mostrar el catalogo completo de prendas con nombre, marca, publico, talla, precio, stock y estado.

    RF02: Consultar la ficha tecnica detallada de una prenda ingresando a su identificador unico (/ropa/id/).

    RF03: Registrar nuevas prendas mediante un formulario validado que asegure el ingreso de campos obligatorios y tipos de datos correctos.

    RF04: Filtrar y buscar prendas en tiempo real por texto (nombre o marca), tipo de publico y categoria.

    RF05: Mostrar un mensaje informativo cuando la busqueda no arroje resultados.

    RF06: Reflejar automaticamente el estado de stock (mostrando "Agotado" cuando las unidades lleguen a 0).

Arquitectura y Persistencia

    Framework: Django (Python)

    Patron: MVT (Model - View - Template)

    Frontend: Django Templates con Bootstrap 5 y Bootstrap Icons

    Persistencia: En memoria RAM. Dado que no se utiliza base de datos relacional para este prototipo, los registros se almacenan dentro de una lista en models.py. Si se detiene o reinicia el servidor, los datos vuelven a los 10 registros base iniciales.


    Estructura del proyecto:

    Django_Lab02/
├── requirements.txt
├── README.md
└── src/
    ├── manage.py
    ├── config/
    │   ├── settings.py
    │   └── urls.py
    ├── core/
    │   └── templates/
    │       └── base.html
    └── store/
        ├── forms.py
        ├── models.py
        ├── urls.py
        ├── views.py
        └── templates/
            └── store/
                ├── prenda_list.html
                ├── prenda_detail.html
                └── prenda_form.html

Guia de Instalacion y Ejecucion Paso a Paso

Clonar el repositorio desde GitHub a la maquina local:
git clone https://github.com/Jesus-Rocha-B/Django_Lab02.git

Ingresar a la carpeta principal del proyecto:
cd Django_Lab02

Crear el entorno virtual de Python:
python3 -m venv venv

Activar el entorno virtual:
En Linux o macOS: source venv/bin/activate
En Windows: venv\Scripts\activate

Instalar los paquetes y dependencias necesarias:
pip install -r requirements.txt

Entrar al directorio del codigo fuente (src):
cd src

Iniciar el servidor local de desarrollo:
python manage.py runserver

Abrir el navegador web e ingresar a la URL del catalogo:
http://127.0.0.1:8000/ropa/