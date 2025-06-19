import tkinter as tk
def on_display():
    print("adel")
    appLabel.config(text = f"Bonjour, {appText.get()} ! Bienvenue dans le monde de la cybersécurité.")

window = tk.Tk()
window.title("Exercice 3")
window.geometry("800x300")

appText = tk.Entry(window, width = 30)
appText.pack()

appButton = tk.Button(window, text="Afficher", command=on_display)
appButton.pack()

appLabel = tk.Label(window, text="")
appLabel.pack()

window.mainloop()