import tkinter as tk
from tkinter import messagebox
import pandas as pd
import main
# Supongamos que tienes las variables primerSemana, top10Estreno y notTop10Estreno con los datos adecuados
df = pd.read_csv("HollywoodMovies.csv")
#Borramos las peliculas que no poseian genero. (ibamos a sacar historia pero al sacar genero el dato quedo bastante completo).
dfMoviesFinal = df.dropna(subset=['Genre'])

#TOP 10 peliculas de OpeningWeekend Taquilleras
primerSemana1 = dfMoviesFinal.sort_values(by="OpeningWeekend", ascending=False)
primerSemana = dfMoviesFinal.sort_values(by="OpeningWeekend", ascending=True)
top10Estreno = primerSemana1.head(10)
notTop10Estreno = primerSemana.head(10)

def mostrar_top10():
    top10_text.delete(1.0, tk.END)
    top10_text.configure(bg='lightgreen') 
    top10_text.insert(tk.END, top10Estreno['Movie'].to_string(index=False))

def mostrar_not_top10():
    not_top10_text.delete(1.0, tk.END)
    not_top10_text.configure(bg='#DC143C') 
    not_top10_text.insert(tk.END, notTop10Estreno['Movie'].to_string(index=False))

# Crear la ventana
root = tk.Tk()
root.title("Top 10 y notTop10 de Películas")

# Crear botones y cuadros de texto
top10_button = tk.Button(root, text="Ver Top 10", command=mostrar_top10)
not_top10_button = tk.Button(root, text="Ver notTop10", command=mostrar_not_top10)

top10_text = tk.Text(root, width=60, height=10, wrap=tk.WORD)
not_top10_text = tk.Text(root, width=60, height=10, wrap=tk.WORD)

# Ubicar los elementos en la ventana
top10_button.pack(pady=5)
top10_text.pack(pady=5)

not_top10_button.pack(pady=5)
not_top10_text.pack(pady=5)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()