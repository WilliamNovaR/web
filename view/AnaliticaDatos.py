import matplotlib.pyplot as plt

#en este documento estan las funciones para la analiticia de datos

#esta funcion sirve para ayudar a la seleccion de que datos y analisis hacer con los datos
def escoger_analis(st, controller, criterio_controler):
    notas = []
    nombres = []
    opcion = st.selectbox("Que analisis quieres hacer?",
                  ('Encontrar Calificacion más alta', 'Estadisticas notas', 'Estadistica criterios'))
    if opcion == 'Encontrar Calificacion más alta':
        mayor_calificacion( st, controller )
    elif opcion == 'Estadisticas notas':
        grafica_notas( st, controller )
    elif opcion == 'Estadistica criterios':
        grifica_criterios(st, controller, criterio_controler)

#esta funcion busca al estudiante con mayor nota e imprime los datos
def mayor_calificacion(st, controller):
    #primero se revisa que se hayan calificado estudiantes de lo contrario hay mensaje de error
    if len(controller.evaluaciones) > 0:
        mejor_calificacion = controller.mejor_calificacion()
        #imprime los tados
        st.subheader("El estudiante con mejor calificiacion es: " + mejor_calificacion.nombre_autor)
        st.subheader("Id:" + mejor_calificacion.id_estudiante)
        st.subheader("Trabajo:" + mejor_calificacion.nombre_trabajo)
        st.subheader("Nota: " + str(round(mejor_calificacion.nota, 1)))
    else:
        st.error("No han calificado a nadie")

#esta funcion grafica las notas finales de todos los estudiantes calificados
def grafica_notas( st, controller ):
    nombres = controller.listar_nombres_calificados() #guarda los nombres de los estudiantes en un arreglo para mostrarlos en la grafica
    notas = controller.listar_notas()# crea un arreglo de las notas de los estudiantes para mostrarlas en una grafica
    #establece las dimenciones de la grafica
    fig = plt.figure(figsize=(10, 5))
    #se establece que datos va a ser el eje x y el y
    plt.bar(nombres, notas)
    #le da un titulo que describe a los datos de x y y
    plt.xlabel("Notas de estudiantes")
    plt.ylabel("Nombre estudiantes")
    plt.title("Notas")
    #imprime tabla
    st.pyplot(fig)

#crea una grafica con la nota promedio de todos los criterios
def grifica_criterios( st, controller, criterio_controler ):
    nombres = criterio_controler.listar_nombre()#guarda los nombres de los criterios en un arreglo para mostrarlos en la grafica
    numeros_criterio = criterio_controler.lista_numero_criterios() #asocia a cada criterio con un numero para asi poder ilustrar la grafica de mejor manera
    notas = criterio_controler.arreglo_criterios()# crea un arreglo de las notas de los criterios para mostrarlas en una grafica
    cantidad = controller.cantidad(criterio_controler) #crea un arreglo con la cantidad de estudiantes por criterio
    controller.promedio_notas_criterios( notas, cantidad, nombres ) #calcula el promedio de notas de los criterios
    #crea e imprime tabla
    fig = plt.figure(figsize=(10, 5))
    plt.bar(numeros_criterio, notas)
    plt.xlabel("Criterios")
    plt.ylabel("Notas criterios")
    plt.title("Notas")
    st.pyplot(fig)
    for iterador in range(len(nombres)):
        st.write(str(numeros_criterio[iterador]) + " = " + nombres[iterador])
