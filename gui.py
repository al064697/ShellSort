# gui.py
import tkinter as tk
from tkinter import messagebox
from shell_sort import shell_sort
import time

# Función para mostrar el proceso y escribir en la ventana sin refrescar el texto
def update_process(arr, i, j, gap, temp):
    description = f"Gap actual: {gap}, comparando arr[{j-gap}] = {arr[j-gap]} con arr[{j}] = {temp}"
    if arr[j - gap] > temp:
        description += f" -> Moviendo {arr[j-gap]} a la posición {j}\n"
    else:
        description += " -> No se mueve\n"
    
    process_text.insert(tk.END, description)  # Insertar el nuevo paso en el área de texto
    root.update()  # Actualizamos la interfaz después de cada paso
    time.sleep(0.5)

# Función que se ejecuta al presionar el botón de orden ascendente o descendente
def sort_numbers(ascending):
    try:
        process_text.delete(1.0, tk.END)  # Limpiar el área de texto antes de iniciar el proceso
        input_data = entry_numbers.get()
        number_list = list(map(int, input_data.split(',')))  # Convertimos la entrada en lista de enteros
        # Llamada al método Shell Sort con una función callback para actualizar el proceso
        shell_sort(number_list, ascending, lambda arr, i, j, gap, temp: update_process(arr, i, j, gap, temp))
        # Mostrar el resultado de la lista ordenada al final del procedimiento
        process_text.insert(tk.END, f"\nLista ordenada: {number_list}\n")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números separados por comas.")

# Función para ir a la pantalla de ordenamiento
def open_sorting_screen():
    intro_frame.pack_forget()
    sorting_frame.pack()

# Crear ventana principal
root = tk.Tk()
root.title("Proyecto Shell Sort")
root.geometry("500x700")
root.configure(bg="white")  # Ventana de fondo blanco

# Portada con los integrantes del equipo
intro_frame = tk.Frame(root, padx=10, pady=10)  # Color de fondo beige suave
intro_frame.pack(fill="both", expand=True)

title_label = tk.Label(intro_frame, text="Bienvenidos al Proyecto Shell Sort", font=("Arial", 26, "bold"))
title_label.pack(pady=(30, 15))

team_label = tk.Label(intro_frame, text="Integrantes del equipo:\n1. Danna Negrón\n2. Hugo Patiño\n3. Sebastian Rios", font=("Arial", 18))
team_label.pack(pady=(0, 30))

description_label = tk.Label(intro_frame, text="El método Shell Sort es un algoritmo de ordenamiento basado en brechas. "
                                               "Reduce el tiempo de ejecución al comparar elementos distantes y luego "
                                               "disminuir la brecha para mejorar el ordenamiento. Es una versión optimizada del "
                                               "ordenamiento por inserción.", wraplength=400, justify="center", font=("Arial", 14))
description_label.pack(pady=(0, 30))

start_button = tk.Button(intro_frame, text="Iniciar Ordenamiento", command=open_sorting_screen, bg="#d1b79c", fg="#6b4c3a", font=("Arial", 16, "bold"), borderwidth=2, relief="raised")
start_button.pack(pady=20)

# Pantalla de ordenamiento
sorting_frame = tk.Frame(root, padx=10, pady=10)

input_label = tk.Label(sorting_frame, text="Ingresa números separados por comas:", font=("Arial", 12))
input_label.pack()

entry_numbers = tk.Entry(sorting_frame, width=50)
entry_numbers.pack()

# Botones para ordenar ascendente y descendente
sort_asc_button = tk.Button(sorting_frame, text="Ordenar Ascendente", command=lambda: sort_numbers(True), bg="#b2d9c5", fg="#6b4c3a", font=("Arial", 14))
sort_asc_button.pack(side="left", padx=10, pady=10)

sort_desc_button = tk.Button(sorting_frame, text="Ordenar Descendente", command=lambda: sort_numbers(False), bg="#f1a7a1", fg="#6b4c3a", font=("Arial", 14))
sort_desc_button.pack(side="left", padx=10, pady=10)

# Nueva área para el proceso en la parte inferior de la ventana
process_frame = tk.Frame(root, bg="black")  # Área de procedimiento en negro
process_frame.pack(side="bottom", fill="both", expand=True)

# Área de texto para describir el proceso (en la parte inferior)
process_text = tk.Text(process_frame, wrap="word", height=10, width=60, bg="black", fg="white")
process_text.pack(padx=10, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()