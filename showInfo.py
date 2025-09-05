lista_bandas = {}

class Concurso:
    def inscribir_banda(self):
        return lista_bandas[self]

    def registrar_evaluacion(self, nombre, puntajes):
        self.nombre = nombre
        self.puntajes = puntajes

    def listar_bandas(self):
        return print(f"{lista_bandas}")
