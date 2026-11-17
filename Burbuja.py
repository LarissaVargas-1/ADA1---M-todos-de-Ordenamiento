import tkinter as tk
from tkinter import messagebox
import time

class AppBurbuja:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordenamiento Burbuja Visual")
        self.datos = []

        # Panel superior para entrada de datos
        frame = tk.Frame(root, pady=10)
        frame.pack()

        tk.Label(frame, text="Números (separados por espacio):").pack(side=tk.LEFT, padx=5)
        self.entrada = tk.Entry(frame, width=30)
        self.entrada.insert(0, "45 12 89 33 67 21 54")
        self.entrada.pack(side=tk.LEFT, padx=5)

        self.btn_iniciar = tk.Button(frame, text="Ordenar", command=self.iniciar, bg="#4CAF50", fg="white")
        self.btn_iniciar.pack(side=tk.LEFT, padx=5)

        # Lienzo para dibujar las barras
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
            for j in range(0, n - i - 1):
                colores = ["#2196F3"] * n
                colores[j] = "#FF5722"      # Comparando (Naranja)
                colores[j + 1] = "#FF5722"
                for k in range(n - i, n):
                    colores[k] = "#4CAF50"  # Ya ordenados (Verde)
                self.dibujar(colores)
                time.sleep(0.35)

                if self.datos[j] > self.datos[j + 1]:
                    self.datos[j], self.datos[j + 1] = self.datos[j + 1], self.datos[j]
                    self.dibujar(colores)
                    time.sleep(0.35)

        self.dibujar(["#4CAF50"] * n)
        self.btn_iniciar.config(state=tk.NORMAL)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AppBurbuja(ventana)
    ventana.mainloop()
