# Manual Técnico

## Entradas Y Salidas
### Entradas
	* Usuario -> sesion.py -> funcion : crear_cuenta -> tipo str
	* Contraseña -> sesion.py -> funcion : crear_cuenta -> tipo str
	* Tipo de cuenta -> -> sesion.py -> funcion : crear_cuenta -> tipo str
	* Usuario -> sesion.py -> funcion : iniciar_sesion -> tipo str
	* Contraseña -> sesion.py -> funcion : iniciar_sesion -> tipo str
	* Id estudiante -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Periodo de evaluacion -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Autor -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Tipo trabajo -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Nombre trabajo -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Nombre director -> InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Nombre coodirector InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* jurado1 InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* jurado2 InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo str
	* Numero de acta InicializarActa.py -> funciones : agregar_datos, editar_calificacion -> tipo int
	* Notas criterios jurado 1 -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo float
	* Notas criterios jurado 2 -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo float
	* Comentarios de cada criterio -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo str
	* Comentario final -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo str
	* Correciones -> Evaluar.py -> funciones: agregar_evaluacion, editar_calificacion -> tipo str
	* Identificador criterio -> ConfigurarCriterios.py -> funcion :  agregar_criterio, editar_criterio -> tipo str
	* Descripcion criterio -> ConfigurarCriterios.py -> funcion :  agregar_criterio, editar_criterio -> tipo str
	* porcentaje pondetacion -> ConfigurarCriterios.py -> funciones :  agregar_criterio, editar_criterio -> tipo str
### Salidas
	*pdf de acta -> CrearActa.py -> funcion : crearActa -> .pdf
	*Grafica con la ota de los estudiantes -> AnaliticaDatos.py -> funcion : grafica_notas -> tipo grafica
	*Grafica promedio de notas criterios -> AnaliticaDatos.py -> funcion : grifica_criterios -> tipo grafica
	*Datos recolectados para el acta -> InformacionActas.py, Evaluar.py -> funciones: 1. listar_actas, 2.editar_calificacion, listar_evaluacion.
	*Datos recolectados criterios -> ConfigurarCriterios.py -> funciones: editar_criterio, eliminar_criterio 

## Principales Clases

### Accionescontroller.py
	Esta clase es la encargada de guardar dentro de arreglos las acciones e icono de las acciones que tendrá disponible
    cada uno de los menús laterales dependiendo del rol de la cuenta que ingrese
    

### ActaControlle.py 
	En esta clase se guardan dentro de un arreglo todas las actas que se generen, esto con la finalidad de tener un registro de las actas
    y poder ver el histórico de estas, además sirve para guardar las actas dentro de un arreglo de manera ordenada y hacer todos los cálculos referentes a las Actas en el backend
    dentro de sus principales métodos encontramos:
       * agregar_acta: metodo creado para agregar elementos al arreglo del método actas
       * Cargar: esta función sirve para cargar en un .json las actas y guardarlas para que no se borren cada vez que se ejecuta el programa
       * leer: lee la información guardada en los json
       * listar_nombre: Da una lista con todos los nombres de los pdfs
        


### CriterioController.py
	En esta clase se guardan dentro de un arreglo todos los criterios para guardarlas, recórrelas y acceder a estas de una manera ordena y rápida
    Sus principales métodos son:
       * agregar_criterios: método para agregar elementos al arreglo
       * ponderacion_final: este método comprueba que el total del porcentaje de ponderado de notas sea el 100%
       * cargar:este método sirve para cargar en un .json los criterios y guardarlas para que no se borren cada vez que se ejecuta el programa
       * leer: lee la información guardada en los json
       * listar_nombre: retorna una lista con los nombres de los criterios
       * lista_numero_criterios: esta función retorna una lista con el número de cada criterio
### CuentaController.py 
	En esta clase guarda dentro de un arreglo todas las cuentas que se crean para guardarlas, recórrelas y acceder a estas de una manera ordena y rápida
    y hacer todos los cálculos referentes a las Actas en el backend, sus principales métodos son:
       * agregar_cuenta: metodo creado para agregar cosas al arreglo cuenta
       * cargar: esta función sirve para guardar las cuentas dentro de un .json
       * leer: lee los datos guardados en el .json


### EvalController.py
	En esta clase se guardan dentro de un arreglo todas las evaluaciones que se crean para guardarlas, recórrelas y acceder a estas de una manera ordena y rápida
    Sus principales métodos son:
       * agregar_evaluacion: agrega las evaluaciones dentro del arreglo
       * cargar: este método sirve para guardar las evaluaciones en un .json para que cada vez que se cierra y abre el programa se guarden los parámetros
       * promedio_notas_criterios: en esta función generamos el promedio de notas de cada criterio
       * cantidad: sirve para saber la cantidad de personas las cuales se les ha calificado un criterio
       * listar_notas: Lista las notas de los estudiantes
       * mejor_calificacion: encuentra al estudiante con mayor calificación
       * istar_nombres_calificados: Da una lista con los nombres de los estudiantes calificados
       * listar_nombres: Da una lista con los nombres de los estudiantes
       * cargar: sirve para guardar las cuentas dentro de un .json
       * leer: lee los datos guardados en el .json
### Acta.py
	Esta clase es la encarga de generar las actas en pdf con los respectivos datos establecidos para esta.

### Calificacion.py
	Esta es la clase de las notas donde se guardan todos los datos ingresados por el usuario en el fronted referente a las notas, además posee funcionalidades para calcular las notas.
### Criterio.py
	Esta clase es donde se establecen todos los datos ingresados por el usuario en el fronted referentes a los criterios para que estos se puedan crear o modificar.
### Cuenta.py
	Esta clase es donde se establecen todos los datos ingresados por el usuario en el fronted referentes a los usuarios para que estos se puedan crear o modificar.
### EvalEstudiantes.py
	Esta clase es donde se establecen todos los datos ingresados por el usuario en el fronted referentes a las evaluaciones para que estos se puedan crear o modificar, además hay funcionalidades para calcular las notas.
## Librerias
	-fpdf = 1.7.2
	-openpyxl
	-streamlit>=1.8.1
	-streamlit-option-menu>=0.3.2
	-pydataxm == 0.2.6
	-Pillow~=9.1.0
	-DateTime~=4.4
	-matplotlib~=3.5.2

## UML link:
https://drive.google.com/file/d/1Jj4yWoMtP5Dk9CHfPb9N6-kSDa2q62J0/view?usp=sharing


