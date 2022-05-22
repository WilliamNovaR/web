#clase creada para almacenar las calificaciones de cada uno de los criterios a evaluar ademas de realziar diversas operaciones con los datos
#como estacer una nota_final, editar_nota_finañ, editar_nota y crear diccinarios

class Calificacion:

    def __int__(self) -> None:
        self.numero_jurados = 0
        self.id_criterio = ""
        self.ponderacion = 0
        self.nota_jurado1 = 0
        self.nota_jurado2 = 0
        self.nota_final = 0
        self.comentario = ""

    #esta aplicacion saca la nota final de un criterio la cual se consigue mediante el promedio de nota del jurado 1 y 2
    def establecer_nota_final(self, nota_jurado1, nota_jurado2,numero_jurados):
        return round( (nota_jurado1 + nota_jurado2) / numero_jurados, 2)

    #esta funcion sirve para el caso que se editen las notas de algun estudiante estas no sean erroenas
    def editar_nota(self, nota, nota_final, ponderacion):
        return nota - (nota_final * ponderacion)

    # esta funcion sirve para el caso que se editen las notas de algun estudiante la nota final no sean erroenas
    def editar_nota_final(self, nota_jurado1, nota_jurado2, numero_jurados ):
        return (nota_jurado1 + nota_jurado2) / numero_jurados

    #sirve para trandormar el objeto en un diccionario y asi guardarlo en json
    def crear_dic(self):
        diccionario = { 'numero_jurados':self.numero_jurados,'id_criterio':self.id_criterio,'ponderacion':self.ponderacion,'nota_jurado1':self.nota_jurado1,'nota_jurado2':self.nota_jurado2,'nota_final':self.nota_final,'comentario':self.comentario }
        return diccionario