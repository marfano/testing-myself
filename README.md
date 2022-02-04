# TestMyself

_Code Kata basado en [este desafío](https://github.com/marfano/tentative-courses) de Nulinga (parte de la entrevista técnica para la posición de Software Engineer)_

## Sinopsis 🚀

_Primer acto: docentes y estudiantes deben poder registrarse, editarse y eliminarse. ¿Motivo? Ser parte de un curso 🤡_

_Segundo acto: quien arme los cursos necesita filtros automáticos. Basta de leer registro a registro, estamos en el SXXI._

_Tercer acto: presento la solución. _ 🌈

* 📢 En Django porque facilita mucho la vida en la POO, 
* 👻 con varios módulos y plugins dando vueltas por ahí ~~y listados en requirements.txt~~,
* ✅ y testeos en Pytest y DjangoTest para ver que todo esté ok 🏖 

_Nombre de la obra? Tentative-courses, donde te listo cursos tentativos filtrando por algunas categorías y cantidades_

Ahora sí: LET'S DO IT

![Esta es una imagen](https://media.giphy.com/media/W1Sx4lnn3tu7wEMabW/giphy.gif)


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋🔧

~~Manos a la terminal~~

Comprobá tu versión de Python (2022? debe ser ~=3.10)

```
python --version
```
Comprobá tu versión de pip (~=22.0.2)

```
pip --version
```

### Instalación 🔧

Porque siempre es mejor trabajar dentro de un entorno de desarrollo 💁🏽‍♀️ vamos a necesitar instalar `venv` 

```
pip install venv
```

Elegí/creá una carpeta e inicializá un entorno: 

```
mkdir environments
cd environments
python -m pip venv myvenv    // donde myvenv es el nombre de tu entorno virtual
```

Activando el entorno 
```
cd myvenv
Scripts/activate
```

Donte estás, cloná el repositorio 🤓 instalá las dependencias del archivo `requirements.txt`  :+1: 

```
pip install -r requirements.txt
```

_No olvides la base de datos! Estoy usando PostgreSQL, pero hace tiempo la discrimiación no va._
Para setearla (y otras configuraciones) creá un archivo `.env` ~~el mío está oculto por un .gitignore~~ y agregá:

```
SECRET_KEY=<Tranquilo vaquero. Ya te digo cómo obtenerla>
DATABASE_NAME=<acá el nombre de tu DB>
DATABASE_USER=<Nombre de usuario de la DB>
DATABASE_PASS=<La password de tu DB>

TEMPLATES=< copy->paste del path de la carpeta `Templates`>

DJANGO_SETTINGS_MODULE=TestMyself.settings
```

_Cómo obtener `SECRET_KEY`?_

No puedo explicarlo mejor que [este post](https://programadorwebvalencia.com/como-generar-un-secret-key-en-django/)


### Getting started 🚀

_Parate en el directorio inicial `/TestMyself` (el que tiene a `manage.py`) y migrá los modelos a la DB_

```
python manage.py migrate
python manage.py makemigrations
```

_Y ahora solo correrlo..._

```
python manage.py runserver
```

_Listo! Corriendo en `localhost:8000` 😁_

![Esta es una imagen](https://media.giphy.com/media/CuMiNoTRz2bYc/giphy.gif)


_Navegá libre y amablemente sopesando que es la versión súper delta..._


## Ejecutando las pruebas ⚙️

_¿Probando los acceptances tests?_

```
pytest -rP
```
_Warning ⚠ posible error de `DJANGO_SETTINGS_MODULE`_
✅Solución✅ En la terminal:
```
set SJANGO_SETTINGS_MODULE=TestMyself.settings
```

## Construido con 🛠️

_Principales herramientas_

* [Python](https://www.python.org/) 🐍- Lenguaje
* [Django](https://www.djangoproject.com/) - El framework web 
* [PostgreSQL](https://www.postgresql.org/) - DB OK :+1:
* [Pytest](https://docs.pytest.org/en/7.0.x/) - TDD SI 😁 ~~(mano a mano con DjangoTest)~~

## Wiki 📖

Puedes encontrar mucho más de cómo funciona este proyecto ~~próximamente~~ en esta [Wiki]() muy betha

![Esta es una imagen](https://media.giphy.com/media/hXCGdsSC3MKuqZv59G/giphy.gif)


## Autores ✒️

_Made-in:_

* **Martina Ramirez** - *This work* - [marfano](https://github.com/marfano)
* **Juani Villarejo** - *Kata-maker* - [jvillarejo](https://github.com/jvillarejo)


## Expresiones de Gratitud 🎁

* A mi hermana por los buenos mates cebados 🧡
* Invitando a quienquiera hablar de Django y POO a una 🍺 o un café ☕ 
* ~~fueron dos semanas intensas de aprender TDD y otras code-cosas~~. 
* Juani, lo admito: amé las referencias a Star Wars 🤓.
* y un largo etc.


---
⌨️ con ❤️ por [marfano](https://github.com/marfano) 😊
