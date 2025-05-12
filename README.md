# Validador y Gestor de Correos.
## Realizado por:

- Alejandra David
- Cristian Baena
- Gabriel Franco

## Funcionalidades:

- **Menú de interacción:** Al ejecutar la aplicación nos encontramos con una interfaz de consola que nos enseña las opciones
disponibles en esta, las cuales son: `Registrar Correos`, `Visualizar Correos`, `Buscar Correos`, y `Salir de la aplicación`.

- **Registrar Correos:** Tal como su nombre lo indica, esta función se encarga de registrar nuevos correos a voluntad del usuario, con la regla de que solo puede registrar dos tipos de dominios específicos, `@utv.edu.co` para profesores y `@estudiante.utv.edu.co` para estudiantes, si el dominio ingresado por el usuario no coincide con los dominios permitidos, el correo no se ingresará al sistema y el usuario deberá ingresar el correo deseado nuevamente.

- **Visualizar Correos:** Esta función se encarga de desplegar en una lista todos los correos registrados en el sistema, haciendo un apartado de profesores y otro de estudiantes para mayor orden y legibilidad.

- **Buscar Correos:** Esta función se encarga de realizar una búsqueda especifica de el correo deseado, al hacer uso de esta función deberá ingresar la dirección de correo que desee buscar, si esta se encuentra en el sistema, se mostrará en pantalla, de lo contrario se mostrará un mensaje de error.

- **Salir de la aplicación:** Al hacer uso de esta función, la aplicación se detendrá por completo y su memoria se reiniciará, eliminando toda la información registrada, ya que este proyecto no cuenta con persistencia de datos.

## Construido con:

[Python 3.11.9]
