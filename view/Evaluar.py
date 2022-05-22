from model.Calificacion import Calificacion

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""

#esta funcion permite califar a un estudiante previmente registrado
def agregar_evaluacion(st, controller, criterios_controller):
    #establecen la calificacion maxima, minima, calificacion para ganar honorificos y calificacion de aprovacion
    nota_maxima = 5.0
    nota_minima = 0.0
    honorificos = 4.5
    aprovacion = 3.5
    lista_nombres = controller.listar_nombres()
    #comprueba que hayan actas iniciadas para calificar
    if len(controller.evaluaciones) < 1:
        st.error( "No hay estudiantes inicializados para calificar" )
    seleccion_estudiante = st.selectbox("Calificar a:", lista_nombres)
    #este ciclo sirve para buscar el estudiante a calificar y llenar sus datos
    for evaluacion_obj in controller.evaluaciones:
        if evaluacion_obj.nombre_autor == seleccion_estudiante:
            lista_calificaciones = [] #se va a usar este arreglo para guardar la informacion y luego pasarlo al objeto ya que si se hace directamente del objeto causa errores debido a la constante actulizacion del streamlit
            criterios = []
            #iniciliza algunos datos de criterios de evaluacion
            for i in range(len(criterios_controller.criterios)):
                criterios.append(criterios_controller.criterios[i].identificador)
                lista_calificaciones.append(Calificacion())
                lista_calificaciones[i].numero_jurados = 2
                lista_calificaciones[i].id_criterio = criterios_controller.criterios[i].identificador
                lista_calificaciones[i].ponderacion = criterios_controller.criterios[i].porcentaje_ponderacion
            #lee los datos de calificacion de los criterios
            contador = 21
            for j in range(len(lista_calificaciones)):
                contador = 2010 + (j + 1)**2
                st.subheader("Criterio " + lista_calificaciones[j].id_criterio)
                lista_calificaciones[j].nota_jurado1 = st.number_input("Nota jurado 1:", key= ( 2 + j),
                                                                       min_value=nota_minima, max_value=nota_maxima)
                contador *= 7 + j
                lista_calificaciones[j].nota_jurado2 = st.number_input("Nota jurado 2:", key=j * (j + contador ), min_value=nota_minima,
                                                                       max_value=nota_maxima)
                lista_calificaciones[j].nota_final = lista_calificaciones[j].establecer_nota_final(lista_calificaciones[j].nota_jurado1, lista_calificaciones[j].nota_jurado2, lista_calificaciones[j].numero_jurados )
                lista_calificaciones[j].comentario = st.text_input("Comentario:", key=(j + contador) * 30, )
                evaluacion_obj.nota = evaluacion_obj.establecer_nota(lista_calificaciones[j].nota_final, lista_calificaciones[j].ponderacion, evaluacion_obj.nota ) # se calcula la nota
                contador += 2
            evaluacion_obj.nota = 0
            for j in range(len(lista_calificaciones)):
                evaluacion_obj.nota = evaluacion_obj.establecer_nota(lista_calificaciones[j].nota_final, lista_calificaciones[j].ponderacion, evaluacion_obj.nota ) # se calcula la nota
            evaluacion_obj.nota = round(evaluacion_obj.nota, 1) #redondea nota a una decima
            #lee comentario final y las correciones
            st.subheader( "Datos Finales" )
            evaluacion_obj.comentario_final = st.text_input("Comentario Final:")
            evaluacion_obj.correciones = st.text_input("Correciones: ")
            #sirve para comrobar si el trabajo merece honorificos o no
            if evaluacion_obj.nota >= honorificos:
                st.subheader( "Recomendaciones honorificos" )
                evaluacion_obj.recomendacion = st.text_input("Recomendación y apreciaciones:")
            st.subheader("Nota final: " + str(evaluacion_obj.nota))
            #nos dice si el trabajo fue aprobado o no dependiendo de la nota final
            if evaluacion_obj.nota > aprovacion:
                st.success("Aprobado")
            else:
                st.error("Reprobado")
            enviado_btn = st.button("Send")
            evaluacion_obj.nota = round(evaluacion_obj.nota, 1) #proxima la nota con un solo decimal

            if enviado_btn:
                evaluacion_obj.calificacion = lista_calificaciones #carga en el objeto las calificaciones
                controller.cargar()
                st.success("Evaluacion agregada exitosamente")
            else:
                st.error("Faltan criterios por calificar!!!")

    return controller

#esta funcion permite escoger si ver o editar las calificaciones

def seleccion( st, controller, criterios_controller ):
    st.title("Ver y editar calificaciones")
    ver_editar = st.selectbox("Que quieres hacer?", ('Ver', 'Editar'))
    estudiantes_nombres = controller.listar_nombres_calificados()  # en este arreglo guardaremos los nombres para luego desplegarlo en un select box
    criterios = criterios_controller.listar_nombre()  # en este arreglo se fuardan los nombres de los riterios para luego desplegarlo en una select boc
    seleccionar_estudiantes = st.selectbox( "Escoge un estudiante:", estudiantes_nombres )
    #comprueba que hayan calificaciones subidas
    if( len(estudiantes_nombres) < 1 ):
        st.error( "No hay estudiantes calificados" )
    if ver_editar == 'Ver':
        listar_evaluacion(st, controller, criterios, seleccionar_estudiantes)
    else:
        editar_calificacion( st, controller, criterios, seleccionar_estudiantes )

def listar_evaluacion(st, controller, criterios, seleccionar_estudiantes):
    honorifico = 4.5
    for evaluacion in controller.evaluaciones:
        if seleccionar_estudiantes == evaluacion.nombre_autor: #comprueba que se va a ver los datos del estudiante seleccionado
            #imprime los datos
            st.subheader("Id autor: " + evaluacion.id_estudiante)
            st.subheader("Periodo evaluacion: " + evaluacion.periodo)
            st.subheader("Nombre autor: " + evaluacion.nombre_autor)
            st.subheader("Tipo de trabajo: " + evaluacion.tipo_trabajo)
            st.subheader("Titulo del trabajo: " + evaluacion.nombre_trabajo)
            st.subheader("Nombre director: " + evaluacion.nombre_director)
            st.subheader("Nombre codirector: " + evaluacion.nombre_codirector)
            st.subheader("Enfasis en: " + evaluacion.enfasis)
            st.subheader("Jurado1 : " + evaluacion.nombre_jurado1)
            st.subheader("Jurado2 : " + evaluacion.nombre_jurado2)
            seleccionar_criterio = st.selectbox("Escoger criterio", criterios, key = int(evaluacion.id_estudiante) )
            #busca e imprime los datos del criterio seleccionado
            for i in evaluacion.calificacion:
                if seleccionar_criterio == i.id_criterio:
                    st.subheader("Nota jurado 1: " + str(i.nota_jurado1))
                    st.subheader("Nota jurado 2: " + str(i.nota_jurado2))
                    st.subheader("Nota del criterio: " + str(i.nota_final))
                    st.subheader("Comentario: ")
                    st.write("" + i.comentario)
            #imprime nota y comentario final del trabjo
            st.subheader("Nota final : " + str(evaluacion.nota))
            st.subheader("Comentario final : " + evaluacion.comentario_final)
            #revisa si la nota fue mayor a 4.5 para desplegar la obcion de recomendaciones y apreciaciones
            if evaluacion.nota >= honorifico:
                st.subheader("Recomendación y apreciaciones: " + evaluacion.recomendacion)

#en caso de escoger la opcion editar permite cambiar los valores del estudiante y sus calificaciones
def editar_calificacion(st, controller, criterios, seleccionar_estudiantes):
    flag = 0
    honorifico = 4.5 # carga la nota de honorifico
    index = 0
    #recorre controlle.evaluaciones para allar al estudiantr al cual le vamos a editar la nota
    for evaluacion in controller.evaluaciones:
        if seleccionar_estudiantes == evaluacion.nombre_autor:
            #muestra los datos para editar del estudiante
            evaluacion.id_estudiante = st.text_input("Id estudiante", value=evaluacion.id_estudiante)
            #controla que no se vayan a poner dos id iguales
            for i in range(len(controller.evaluaciones)):
                if controller.evaluaciones[i].id_estudiante == evaluacion.id_estudiante and i != index:
                    flag = 1
            #imprime más datos que podran ser editados
            evaluacion.periodo = st.text_input("Periodo de evaluacion", value=evaluacion.periodo)
            evaluacion.nombre_autor = st.text_input("Nombre del autor", value=evaluacion.nombre_autor)
            #este if sirve para saber cual es el valor con el que se guardo para que a la hora de editar esta dato sea el seleccionado
            if evaluacion.tipo_trabajo == 'Aplicado':
                evaluacion.tipo_trabajo = st.selectbox("Tipo de trabajo", ('Aplicado', 'Investigacion'))
            else:
                evaluacion.tipo_trabajo = st.selectbox("Tipo de trabajo", ('Aplicado', 'Investigacion'), index=1)
            # permite cambiar el titulo del trabajo y el director
            evaluacion.nombre_trabajo = st.text_input("Nombre del trabajo", value=evaluacion.nombre_trabajo)
            evaluacion.nombre_director = st.text_input("Nombre del director", value=evaluacion.nombre_director)
            st.write("codirector?")
            # este if sirve para saber cual es el valor con el que se guardo para que a la hora de editar esta dato sea el seleccionado y permita agregar o no codirector
            if evaluacion.nombre_codirector == "No aplica":
                coodirector = st.selectbox("El trabajo tiene codirector?", ('Si', 'No'), index=1)
            else:
                coodirector = st.selectbox("El trabajo tiene codirector?", ('Si', 'No'))
            if coodirector == 'Si':
                evaluacion.nombre_codirector = st.text_input("Nombre del codirector",
                                                                         value=evaluacion.nombre_codirector)
            #permite editar otros datos
            evaluacion.enfasis = st.text_input("Enfasis en:", value=evaluacion.enfasis)
            evaluacion.nombre_jurado1 = st.text_input("Nombre del jurado1", value=evaluacion.nombre_jurado1)
            evaluacion.nombre_jurado2 = st.text_input("Nombre del jurado2", value=evaluacion.nombre_jurado2)
            seleccionar_criterio = st.selectbox("Escoger criterio", criterios) #crea select box para seleccionar criterio a esditar
            for i in evaluacion.calificacion:
                if seleccionar_criterio == i.id_criterio: #busca el criterio a seleccionar
                    evaluacion.nota = evaluacion.editar_nota1( evaluacion.nota, i.nota_final, i.ponderacion ) #debido a que la info se actuliza constantemente para editar errores cada vez que se actualiza la nota se le resta la inicial para que esta no se sume con la nueva que van a poner
                    #imprime mas datos de la calificacion y acta
                    i.nota_jurado1 = st.number_input("Nota jurado 1: ", value=i.nota_jurado1)
                    i.nota_jurado2 = st.number_input("Nota jurado 2: ", value=i.nota_jurado2)
                    i.comentario = st.text_input("Comentario ", value=i.comentario)
                    i.nota_final = i.editar_nota_final( i.nota_jurado1, i.nota_jurado2, i.numero_jurados )
                    evaluacion.nota = evaluacion.editar_nota(evaluacion.nota, i.nota_final, i.ponderacion) # se agrega la nueva nota
            st.subheader( "Datos finales" )
            evaluacion.comentario_final = st.text_input("Comentario final", value=evaluacion.comentario_final)
            if evaluacion.nota >= honorifico: #mira si debe desplegar la opcion de los trabjos con nota mayor a 4.5
                st.subheader( "Recomendaciones honorificos" )
                evaluacion.recomendacion = st.text_input("Recomendación y apreciaciones: ",
                                                             value=evaluacion.recomendacion)
        index += 1
        #en caso que la id sea repetida salta el error y desactiva el boton
    if flag == 1:
        st.error( "Id repetida" )
        #en caso que todo sea valido se activa el boton para generar cambios
    else:
        enviar_btn = st.button("Editar", key = 2 * 11 )
        if enviar_btn and flag == 0:
            evaluacion.nota = round(evaluacion.nota, 1)
            controller.cargar()
            st.success("Cambio realizado")



