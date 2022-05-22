import json

#clase creada para guardar datos para el acta

class EvaluacionEstudiante:

    def __init__(self) -> None:
        super().__init__()

        # Datos de toda evaluacion
        self.calificacion = []
        self.id_estudiante = ""
        self.periodo = ''
        self.nombre_autor = ""
        self.nombre_trabajo = ""
        self.tipo_trabajo = ""
        self.nombre_director = ""
        self.nombre_codirector = "No aplica"
        self.enfasis = ''
        self.nombre_jurado1 = " "
        self.nombre_jurado2 = " "
        self.inicilizar = 0
        self.nota = 0.0
        self.comentario_final = ""
        self.correciones = ""
        self.recomendacion = ''

    # esta funcion sirce para establecer la nota final de cada estidiante
    def establecer_nota(self, nota_final, ponderacion, nota ):
        return (nota_final * ponderacion) + nota

    #esta funcion nos ayuda a la hora de querer editar las notas de los estudiantes para que estas no sean erroenas
    def editar_nota(self, nota, nota_final, ponderacion):
        return nota + (nota_final * ponderacion)

    #A la hora de editar la nota esta nos ayuda a poder restarle los valores iniciales de la nota del criterio para que no sea sumadas con los nuevos datos
    #y genere un error de calculos
    def editar_nota1(self, nota, nota_final, ponderacion):
        return nota - (nota_final * ponderacion)

    #esta funcion sirve para poder guardar el objeto en un json y asi generar memoria
    def guardar_calificaciones(self):
        lista = []
        for calificaciones in self.calificacion:
            lista.append(calificaciones.crear_dic())
        return lista

