import json
from model.Criterio import Criterio

#esta clase sirve para guardar, acceder y manejar todo lo relacionado con criterios

class CriterioController:
    #se crean los metodos principales y se establecen los criterios por defecto
    def __init__(self) -> None:
        super().__init__()
        self.criterios = []
        criterio = Criterio("Desarrollo y profundidad en el tratamiento del tema", "", 0.20 )
        self.criterios.append( criterio )
        criterio = Criterio("Desafio academico y cientifico del tema", "", 0.15)
        self.criterios.append(criterio)
        criterio = Criterio("Cumplimiento de los objetivos propuestos", "", 0.10)
        self.criterios.append(criterio)
        criterio = Criterio("Creatividad e innovacion de las soluciones y desarrollos propuestos", "" , 0.10)
        self.criterios.append(criterio)
        criterio = Criterio("Validez de los resultados y concluciones", "", 0.20)
        self.criterios.append(criterio)
        criterio = Criterio("Manejo y procedimiento de la informacion y bibliografia", "", 0.10)
        self.criterios.append(criterio)
        criterio = Criterio("Calidad y presentacion del documento escrito ", "", 0.075)
        self.criterios.append(criterio)
        criterio = Criterio("Presentacion oral", "", 0.075)
        self.criterios.append(criterio)

    #funcion para agregar elementos a el arreglo
    def agregar_criterios(self, criterios_obj):
        self.criterios.append(( criterios_obj ))

    #esta funcion comprueba que el total del porcentaje de ponderado de notas sea el 100%
    def ponderacion_final(self):
        suma = 0
        #suma todos los pocentajes de ponderacion y si son mayores que uno arroja una ecepcion
        for criterio in self.criterios:
            if suma + criterio.porcentaje_ponderacion <= 1:
                suma += criterio.porcentaje_ponderacion
            else:
                raise ValueError( "la sumatoria de los porcentajes de ponderacion de los criterios superan el 100%" )
        return suma

    # esta funcion sirve para cargar en un .json los criterios y guardarlas para que no se borren cada vez que se ejecuta el programa
    def cargar(self):
        lista = []
        # convierte en un diccionario los criterios para poderlos cargar en el .json
        for i in self.criterios:
            diccionario = {'identificador': '', 'descripcion': '', 'porcentaje_ponderacion': ''}
            diccionario['identificador'] = i.identificador
            diccionario['descripcion'] = i.descripcion
            diccionario['porcentaje_ponderacion'] = i.porcentaje_ponderacion
            lista.append(diccionario)
        # carga la informacion dentro del .json
        with open('data_criterios.json', 'w') as outfile:
            json.dump(lista, outfile)

    #lee los dostos que esten cargados en json
    def leer(self):
        with open('data_criterios.json') as json_file: #abre el archivo json
            data = json.load(json_file) # se guarda la info del json en una variable
            lista = []
            #transormamos los diciconarios en objetos
            for crear in data:
                cargar_cuenta = Criterio(crear['identificador'], crear['descripcion'], crear['porcentaje_ponderacion'])
                lista.append(cargar_cuenta)
        self.criterios = lista #los carga en el programa

    #retorna una lista con los nombres de los criterios
    def listar_nombre(self):
        criterios = []
        for criterio in self.criterios:
            criterios.append(criterio.identificador)
        return criterios

    #esta funcion rotarna una lista con el numero de cada criterio
    def lista_numero_criterios(self):
        numeros_criterio = []
        for i in range(len(self.criterios)):
            numeros_criterio.append(i + 1)  # establece un numero para cada criterio
        return numeros_criterio

    def arreglo_criterios(self):
        notas = []
        for name in self.criterios:
            notas.append(0)  # crea los espacios en el arreglo para guardar el promedio de notas
        return notas



