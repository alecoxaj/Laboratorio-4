import tkinter as tk

class Participante:
    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        return f"{self.nombre} - {self.institucion}"


class BandaEscolar(Participante):
    categorías = ["Primaria", "Básico", "Diversificado"]
    criterio = ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]

    def __init__(self, nombre, institucion, categoria):
        super().__init__(nombre, institucion)
        if categoria not in BandaEscolar.categorías:
            raise ValueError("Categoria inválida.")
        self._categoria = categoria
        self._puntajes = {}

    def registrar_puntajes(self, puntajes):
        if set(puntajes.keys()) != set(BandaEscolar.criterio):
            raise ValueError("Faltan criterios")
        for v in puntajes.values():
            if v < 0 or v > 10:
                raise ValueError("Los puntajes deben ser entre 0 y 10")
        self._puntajes = puntajes

    @property
    def total(self):
        return sum(self._puntajes.values()) if self._puntajes else 0

    def mostrar_info(self):
        if self._puntajes:
            return f"{super().mostrar_info()} - {self._categoria} - Total: {self.total}"
        else:
            return f"{super().mostrar_info()} - {self._categoria} - Sin evaluación"


class Concurso:
    def __init__(self, nombre, fecha):
        self._nombre = nombre
        self._fecha = fecha
        self.bandas = {}

    def inscribir_banda(self, banda):
        if banda.nombre in self.bandas:
            raise ValueError("Ya existe una banda con ese nombre")
        self.bandas[banda.nombre] = banda

    def registrar_evaluacion(self, nombre, puntajes):
        self.bandas[nombre].registrar_puntajes(puntajes)

    def listar_bandas(self):
        return [b.mostrar_info() for b in self.bandas.values()]

    def ranking(self):
        return sorted(self.bandas.values(), key=lambda b: b.total, reverse=True)

def inscribir_banda():
    print("Se abrió la ventana: Inscribir Banda")
    ventana_inscribir = tk.Toplevel(ventana)
    ventana_inscribir.title("Inscribir Banda")
    ventana_inscribir.geometry("400x300")
    etiqueta = tk.Label(ventana_inscribir, text="Escribe el nombre de la banda")
    etiqueta.pack(pady=5)

def registrar_evaluacion():
    print("Se abrió la ventana: Registrar Evaluación")
    ventana_eval = tk.Toplevel(ventana)
    ventana_eval.title("Registrar Evaluación")
    ventana_eval.geometry("400x300")

def listar_bandas():
    print("Se abrió la ventana: Listado de Bandas")
    ventana_listado = tk.Toplevel(ventana)
    ventana_listado.title("Listado de Bandas")
    ventana_listado.geometry("400x300")

def ver_ranking():
    print("Se abrió la ventana: Ranking Final")
    ventana_ranking = tk.Toplevel(ventana)
    ventana_ranking.title("Ranking Final")
    ventana_ranking.geometry("400x300")

def salir():
    print("Aplicación cerrada")
    ventana.quit()

ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
ventana.geometry("500x300")

barra_menu = tk.Menu(ventana)

menu_opciones = tk.Menu(barra_menu, tearoff=0)
menu_opciones.add_command(label="Inscribir Banda", command=inscribir_banda)
menu_opciones.add_command(label="Registrar Evaluación", command=registrar_evaluacion)
menu_opciones.add_command(label="Listar Bandas", command=listar_bandas)
menu_opciones.add_command(label="Ver Ranking", command=ver_ranking)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

ventana.config(menu=barra_menu)

etiqueta = tk.Label(
    ventana,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 12, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)

ventana.mainloop()
