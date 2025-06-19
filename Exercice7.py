import tkinter as tk
def on_click():
    print(f"{appText.get(1.0, tk.END)}")

window = tk.Tk()
window.title("Exercice 7")
window.geometry("800x300")

appText = tk.Text(window, height=10, width=45)
appText.pack()

appButton = tk.Button(window, text="Afficher l’alerte", width=45, command=on_click)
appButton.pack()
# lancer mon application
window.mainloop()