import json
from model.EvalEstudiante import EvaluacionEstudiante
from model.Calificacion import Calificacion

#En este clase se guardan dentro de un arreglo todas las evaluaciones que se crean para guardarlas, recorrelas y acceder a estas de una manera ordena y rapida

class EvaluadorController:
    def __init__(self) -> None:
        super().__init__()
        self.evaluaciones = []

    #agrega las evaluaciones dentro del arreglo
    def agregar_evaluacion(self, evaluacion_obj):
        self.evaluaciones.append(evaluacion_obj)

    # esta funcion sirve para guardar las evaluaciones en un .json para que cada vez que se cierra y abre el programa se guarden los parametros
    def cargar(self):
        lista = []
        # se transforma a los objetos en diccionarios para poder cargarlos en el .json
        for i in self.evaluaciones:
            diccionario = {'calificacion': [], 'id_estudiante': '', 'periodo': '', 'nombre_autor': '',
                           'nombre_trabajo': '', 'tipo_trabajo': '', 'nombre_director': '', 'nombre_codirector': '',
                           'enfasis': '', 'nombre_jurado1': '', 'nombre_jurado2': '', 'inicilizar': '', 'nota': '',
                           'comentario_final': '', 'correciones': '', 'recomendacion': ''}
            diccionario['calificacion'] = i.guardar_calificaciones()
            diccionario['id_estudiante'] = i.id_estudiante
            diccionario['periodo'] = i.periodo
            diccionario['nombre_autor'] = i.nombre_autor
            diccionario['nombre_trabajo'] = i.nombre_trabajo
            diccionario['tipo_trabajo'] = i.tipo_trabajo
            diccionario['nombre_director'] = i.nombre_director
            diccionario['nombre_codirector'] = i.nombre_codirector
            diccionario['enfasis'] = i.enfasis
            diccionario['nombre_jurado1'] = i.nombre_jurado1
            diccionario['nombre_jurado2'] = i.nombre_jurado2
            diccionario['inicilizar'] = i.inicilizar
            diccionario['nota'] = i.nota
            diccionario['comentario_final'] = i.comentario_final
            diccionario['correciones'] = i.correciones
            diccionario['recomendacion'] = i.recomendacion
            lista.append(diccionario)
        with open('data_calificaciones.json', 'w') as outfile: #se cargan los datos en data_calificaciones.json
            json.dump(lista, outfile)

    # Lee la informacion guardad en el .json
    def leer(self):
        with open('data_calificaciones.json') as json_file: # abre el archivo
            data = json.load(json_file) # se guarda la info en una variable
            arreglo = []
            for cargar in data:
                lista = []
                evaluaciones = EvaluacionEstudiante()
                #se cargan los archivos en un diccionario
                for datos in cargar['calificacion']:
                    calificacion = Calificacion()
                    calificacion.numero_jurados = datos['numero_jurados']
                    calificacion.id_criterio = datos['id_criterio']
                    calificacion.ponderacion = datos['ponderacion']
                    calificacion.nota_jurado1 = datos['nota_jurado1']
                    calificacion.nota_jurado2 = datos['nota_jurado2']
                    calificacion.nota_final = datos['nota_final']
                    calificacion.comentario = datos['comentario']
                    lista.append(calificacion)
                evaluaciones.calificacion = lista
                evaluaciones.id_estudiante = cargar['id_estudiante']
                evaluaciones.periodo = cargar['periodo']
                evaluaciones.nombre_autor = cargar['nombre_autor']
                evaluaciones.nombre_trabajo = cargar['nombre_trabajo']
                evaluaciones.tipo_trabajo = cargar['tipo_trabajo']
                evaluaciones.nombre_director = cargar['nombre_director']
                evaluaciones.nombre_codirector = cargar['nombre_codirector']
                evaluaciones.enfasis = cargar['enfasis']
                evaluaciones.nombre_jurado1 = cargar['nombre_jurado1']
                evaluaciones.nombre_jurado2 = cargar['nombre_jurado2']
                evaluaciones.inicilizar = cargar['inicilizar']
                evaluaciones.nota = cargar['nota']
                evaluaciones.comentario_final = cargar['comentario_final']
                evaluaciones.correciones = cargar['correciones']
                evaluaciones.recomendacion = cargar['recomendacion']
                arreglo.append(evaluaciones)
            self.evaluaciones = arreglo # se carga en el programa

    #da una lista con los nombre de los estudiantes
    def listar_nombres(self):
        lista_nombres = []
        for evaluaciones in self.evaluaciones:
            lista_nombres.append(evaluaciones.nombre_autor)
            if len(evaluaciones.calificacion) > 0:  # este if sirve para saber si si ya se califico un estudiante y no calificarlo dos veces
                lista_nombres.pop()
        return lista_nombres

    # Da una lista con los nombres de los estudiantes calificados
    def listar_nombres_calificados(self):
        lista_nombres = []
        for nombres in self.evaluaciones:
            if len(nombres.calificacion) > 0:
                lista_nombres.append(
                    nombres.nombre_autor)  # el ciclo recorre el arreglo que tiene todas las calificaciones y guarda en el arreglo los nombres calificados
        return lista_nombres

    # encuentra al estudiante con mayor calificacion
    def mejor_calificacion(self):
        mejor_calificacion = EvaluacionEstudiante()
        # recorre todos los estudiantes calificados para buscar el que tenga mayor nota final
        for i in self.evaluaciones:
            if i.nota > mejor_calificacion.nota:
                mejor_calificacion = i
        return mejor_calificacion

    #Lista las notas de los estudiantes
    def listar_notas(self):
        notas = []
        for i in self.evaluaciones:
            # revisa que los nombres que se van a agregar a la grafica ya esten calificados y no solo inicilizados
            if len(i.calificacion) > 0:
                notas.append(i.nota)
        return notas

#esta funcion sirve para saber la cantidad de persolas las cuales se les ha acalidicado un criterio
    def cantidad(self, criterios_controller):
        cantidad = []
        for i in range( len(criterios_controller.criterios) ):
            cantidad.append(0) #creamos un erragglo con el mismo tamaño del arreglos de criterios_controller.criterios
        #es ciclo sirve para comparar los criterios calificados con los critetrios que se tengan establecidos en el sistemas
        #para saber cuantas personas tienen calificado cada criterio y asi con este numero sacar el promedio de nota de
        #cada criterio
        for l in range(len(criterios_controller.criterios)):
            for j in range( len(self.evaluaciones) ):
                for k in range( len( self.evaluaciones[j].calificacion ) ):
                    if criterios_controller.criterios[l].identificador == self.evaluaciones[j].calificacion[k].id_criterio : #se compara que el criterio seleccionado y los guardados sean los mismos para asi sumar uno a la cantidad de personas con este criterio
                        cantidad[l] +=1
        return cantidad

    #en esta funcion generamos el promedio de notas de cada criterio
    def promedio_notas_criterios(self, notas, cantidad, nombres):
        #comparamos los nombres de los criterios calificados con los que esten establecidos en el sistema para asi poder
        #comprobar los promedios de los criterios establecios por el sistema y/o Director/a
        for j in range(len(nombres)):
            for i in range(len(self.evaluaciones)):
                for l in range( len(self.evaluaciones[i].calificacion) ):
                    if len(self.evaluaciones[i].calificacion) > 0 :
                        if nombres[j] == self.evaluaciones[i].calificacion[l].id_criterio:
                            notas[j] += self.evaluaciones[i].calificacion[l].nota_final
        #dividimos la sumatoria de las notas por creite en tre la cantidad de estudiantes con este criterio calificado
        #para asi sacar el promedio de cafa criterio
        for k in range(len(notas)):
            #evitamos el error de la division entre 0, adiganandole como promedio 0 a los criterio que no tienen ninguna calificacion
            if cantidad[k] == 0:
                notas[k] = 0
            else:
                notas[k] /= cantidad[k]