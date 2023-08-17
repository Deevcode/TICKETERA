# TICKETERA
## REPORTES EN TICKETERA PERSONAL

### CONFIGURACION DEL ENTORNO VIRUAL

CONFIGURACIONES:

La aplicación se ha desarrollado utilizando el framework Django y está programada en Python. Está configurada para utilizar el motor de base de datos Oracle y se ejecutará en un servidor local.

Para poder ejecutar la aplicación, es necesario tener instalados Django 4.1 y Python 3.10. Es importante destacar que se deben utilizar estas versiones específicas. Se recomienda trabajar en un entorno de desarrollo virtual, ya que el archivo requirements.txt contiene la versión de Django que se utilizará. A continuación, se proporcionarán los enlaces necesarios para realizar las instalaciones.

        PYTHON: https://www.python.org/downloads/
        DJANGO: https://www.djangoproject.com/download/
        VIRTUAL-ENV: https://docs.python.org/es/3/tutorial/venv.html

Una vez que hayamos descargado todo, procederemos a clonar el repositorio en GitHub. Para ello, abre la consola bash en el directorio en el que deseas clonar el repositorio y ejecuta el siguiente comando en la consola:

        git clone https://github.com/Deevcode/TICKETERA .

Una vez que hayas clonado el repositorio, abre la carpeta en tu editor de código preferido. A continuación, crea un archivo llamado ".env" en la raíz del proyecto. En este archivo, deberás configurar el acceso a la base de datos. Por motivos de seguridad, utilizamos variables de entorno para esta configuración de información sensible. Es importante destacar que este proyecto está diseñado para mostrar una demostración del aplicativo.

Ahora creamos nuestros entornos viruales de desarrollo, en este caso crearemos uno llamado "ticketera".

        virtualenv ticketera
        
Luego activamos el entorno de desarrollo con el siguiente comando.
 
        ticketera\Scripts\activate
 
Ahora que has creado el entorno, procedemos a instalar todas las dependencias del proyecto que se encuentran en el archivo "requirements.txt". Esto nos permitirá ejecutar la aplicación sin problemas. Ejecuta el siguiente comando para instalar las dependencias:

        pip install -r requirements.txt
        
Asegúrate de tener instalado el gestor de base de datos SQL Developer en su versión 23, ya que te permitirá visualizar los datos del aplicativo. Una vez que hayas confirmado que las configuraciones están correctamente establecidas, procedemos a crear las migraciones utilizando los siguientes comandos:

        python manage.py makemigrations
        python manage.py migrate
        
### EJECUCION DE LA APLICACION

Ahora que has completado todas las configuraciones y migraciones, procedemos a ejecutar la aplicación utilizando el siguiente comando:

        python manage.py runserver