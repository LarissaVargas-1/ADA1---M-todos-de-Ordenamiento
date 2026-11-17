import tkinter as tk
from tkinter import messagebox
import time

class AppSeleccion:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordenamiento por Selección Visual")
        self.datos = []

        frame = tk.Frame(root, pady=10)
        frame.pack()

        tk.Label(frame, text="Números (separados por espacio):").pack(side=tk.LEFT, padx=5)
        self.entrada = tk.Entry(frame, width=30)
        self.entrada.insert(0, "34 78 12 56 95 23 41")
        self.entrada.pack(side=tk.LEFT, padx=5)

        self.btn_iniciar = tk.Button(frame, text="Ordenar", command=self.iniciar, bg="#4CAF50", fg="white")
        self.btn_iniciar.pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(root, width=600, height=350, bg="white")
        self.canvas.pack(padx=10, pady=10)

    def dibujar(self, colores):
        self.canvas.delete("all")
        if not self.datos:
            return
        ancho_canvas = 600
        alto_canvas = 350
        n = len(self.datos)
        ancho_barra = (ancho_canvas - 40) / n
        max_val = max(self.datos)

        for i, val in enumerate(self.datos):
            x0 = 20 + i * ancho_barra
            y0 = alto_canvas - (val / max_val) * (alto_canvas - 50)
            x1 = x0 + ancho_barra - 4
            y1 = alto_canvas - 20

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colores[i], outline="")
            self.canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(val), font=("Arial", 10, "bold"))
        self.root.update()

    def iniciar(self):
        try:
            self.datos = [int(x) for x in self.entrada.get().split()]
            if len(self.datos) < 2:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingresa al menos 2 números enteros válidos.")
            return

        self.btn_iniciar.config(state=tk.DISABLED)
        n = len(self.datos)

        for i in range(n):
            idx_min = i
            for j in range(i + 1, n):
                colores = ["#4CAF50" if k < i else "#2196F3" for k in range(n)]
                colores[idx_min] = "#E91E63"  # Mínimo actual (Rosa)
                colores[j] = "#FF5722"        # Revisando (Naranja)
                self.dibujar(colores)
                time.sleep(0.35)

                if self.datos[j] < self.datos[idx_min]:
                    idx_min = j

            self.datos[i], self.datos[idx_min] = self.datos[idx_min], self.datos[i]
            colores = ["#4CAF50" if k <= i else "#2196F3" for k in range(n)]
            self.dibujar(colores)
            time.sleep(0.35)

        self.dibujar(["#4CAF50"] * n)
        self.btn_iniciar.config(state=tk.NORMAL)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AppSeleccion(ventana)
    ventana.mainloop()
