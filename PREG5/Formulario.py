from Objeto import Objeto

class Formulario: 

    def __init__(self):
        pass

    def rellenar(self, objeto):
        self.nombre = objeto.nombre
        self.categoria = objeto.categoria
        self.marca = objeto.marca
        self.tamanio = objeto.tamanio
        self.anio_de_creacion = objeto.anio_de_creacion
