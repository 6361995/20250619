import tkinter as tk

def on_check():
    if appIntvar.get() == 1:
        appLabel.config(text = "Mode sécurisé activé")
    else:
        appLabel.config(text = "Mode standard activé")
window = tk.Tk()
window.title("Exercice 5")
window.geometry("800x300")

appIntvar = tk.IntVar()

appcheckbutton = tk.Checkbutton(window, text = "Activer le mode sécurisé", variable=appIntvar)
appcheckbutton.pack()
appButton = tk.Button(window, text = "Vérifier", command = on_check)
appButton.pack()

appLabel = tk.Label(window, text="")
appLabel.pack()

window.mainloop()