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





    def registrar_evaluacion():
        if not concurso.bandas:
            messagebox.showwarning("Aviso", "No hay bandas inscritas")
            return

        nombre = simpledialog.askstring("Evaluación", "Nombre de la Banda a evaluar:")
        if nombre not in concurso.bandas:
            messagebox.showerror("Error", "Esa banda no está escrita.")
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





