import json
from model.Cuenta import Cuenta

#esta clase sirve para guardar las cuentas dentro de un arreglo de manera ordenada y hacer todos los calculos referentes a las Actas en el backend


class Cuentas:
    def __init__(self) -> None:
        super().__init__()
        self.cuentas = []

    #funcion creada para agregar cosas al arreglo cuenta
    def agregar_cuenta(self, acta_obj):
        self.cuentas.append(acta_obj)

    # esta funcion sirve para guardar las cuentas dentro de un .json
    def cargar(self):
        lista = []
        # se recorren todos los elementos dentro de cuentaController para guardarlo en un diccionario para poder guardarlo en el .json
        for i in self.cuentas:
            diccionario = {'usuario': '', 'contrasena': '', 'tipo': ''}
            diccionario['usuario'] = i.usuario
            diccionario['contrasena'] = i.contrasena
            diccionario['tipo'] = i.tipo
            lista.append(diccionario)
        # se abre y se guarda el diccionario en el .json
        with open('data_cuentas.json', 'w') as outfile:
            json.dump(lista, outfile)

    #lee los datos guardados en el json
    def leer(self):
        with open('data_cuentas.json') as json_file:#abre el archivo json
            data = json.load(json_file)# se guarda la info del json en una variable
            lista = []
            for crear in data:
                cargar_cuenta = Cuenta()
                cargar_cuenta.usuario = crear['usuario']
                cargar_cuenta.contrasena = crear['contrasena']
                cargar_cuenta.tipo = crear['tipo']
                lista.append(cargar_cuenta)
        self.cuentas = lista