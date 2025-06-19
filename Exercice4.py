import tkinter as tk
from tkinter import messagebox

def on_display(action):
    try:
        value1 = int(appText1.get())
        value2 = int(appText2.get())
        if action == "+":
            res = value1 + value2
        elif action == "-":
            res = value1 - value2
        elif action == "x":
            res = value1 * value2
        else:
            res = value1 / value2
    except ValueError:
        messagebox.showerror(title='Erreur', message='Il faut saisir un entier')
    except ZeroDivisionError:
        messagebox.showerror(title='Erreur', message='Division par zéro interdite')

window = tk.Tk()
window.title("Exercice 4")
window.geometry("800x300")

appText1 = tk.Entry(window, width = 30)
appText1.pack()
appText2 = tk.Entry(window, width = 30)
appText2.pack()

appButtonAdd = tk.Button(window, text="+", command=lambda:on_display("+"), width=1, height=1)
appButtonAdd.pack()
appButtonMin = tk.Button(window, text="-", command=lambda:on_display("-"), width=1, height=1)
appButtonMin.pack()
appButtonMul = tk.Button(window, text="x", command=lambda:on_display("x"), width=1, height=1)
appButtonMul.pack()
appButtonDiv = tk.Button(window, text="/", command=lambda:on_display("/"), width=1, height=1)
appButtonDiv.pack()

appLabel = tk.Label(window, text="")
appLabel.pack()

window.mainloop()