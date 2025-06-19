import tkinter as tk

def on_clear():
    appText.delete(1.0, tk.END)

window = tk.Tk()
window.title("Exercice 8")
window.geometry("800x300")

menu_bar = tk.Menu(window, title = "Exercice 8")

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Effacer", command=on_clear)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=window.quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)

appText = tk.Text(window, width=100)
appText.pack()

window.mainloop()