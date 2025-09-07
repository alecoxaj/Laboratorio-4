import tkinter as tk
from tkinter import messagebox, simpledialog

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

class ConcursoBandasApp:
    def __init__(self):
        self.concurso = Concurso("Concurso de Bandas", "2025-09-14")

        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        nombre = simpledialog.askstring("Inscripción", "Nombre de la Banda:")
        institucion = simpledialog.askstring("Inscripción", "Institución:")
        categoria = simpledialog.askstring("Inscripción", "Categoria (Primaria, Básico, Diversificado")

        if not nombre or not institucion or not categoria:
            return

        try:
            banda = BandaEscolar(nombre, institucion, categoria)
            self.concurso.inscribir_banda(banda)
            messagebox.showinfo("Éxito", f"Banda '{nombre}' inscrita correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def registrar_evaluacion(self):
        if not self.concurso.bandas:
            messagebox.showwarning("Aviso", "No hay bandas inscritas")
            return

        nombre = simpledialog.askstring("Evaluación", "Nombre de la Banda a evaluar:")
        if not nombre:
            return
        if nombre not in self.concurso.bandas:
            messagebox.showerror("Error", "Esa banda no está inscrita.")
            return

        puntajes = {}
        for criterio in BandaEscolar.criterio:
            valor = simpledialog.askinteger("Evaluación", f"Puntaje de {criterio} (0-10):", minvalue=0, maxvalue=10)
            if valor is None:
                return
            puntajes[criterio] = valor

        try:
            self.concurso.registrar_evaluacion(nombre, puntajes)
            messagebox.showinfo("Éxito", f"Puntajes registrados para '{nombre}'")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def listar_bandas(self):
        if not self.concurso.bandas:
            messagebox.showwarning("Listado", "No hay bandas inscritas.")
        else:
            lista = "\n".join(self.concurso.listar_bandas())
            messagebox.showinfo("Listado de Bandas", lista)

    def ver_ranking(self):
        if not self.concurso.bandas:
            messagebox.showwarning("Ranking", "No hay bandas inscritas.")
        else:
            ranking = self.concurso.ranking()
            texto = ""
            for i, b in enumerate(ranking, 1):
                texto += f"{i} {b.nombre} - {b.institucion} - {b._categoria} - Total: {b.total}\n"
            messagebox.showinfo("Ranking Final", texto)


if __name__ == "__main__":
    ConcursoBandasApp()







