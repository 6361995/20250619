import tkinter as tk

def on_check():
    appLabel.config(text = f"Vous avez choisi la méthode : {appStringvsar.get()}")
window = tk.Tk()
window.title("Exercice 6")
window.geometry("800x300")

appStringvsar = tk.StringVar()

appButton1 =tk.Radiobutton(window,text="César",variable=appStringvsar,value="César")
appButton1.pack()
appButton2 =tk.Radiobutton(window,text="Inversion",variable=appStringvsar,value="Inversion")
appButton2.pack()
appButton3 =tk.Radiobutton(window,text="ROT13",variable=appStringvsar,value="ROT13")
appButton3.pack()

appButton = tk.Button(window, text = "Confirmer", command = on_check)
appButton.pack()

appLabel = tk.Label(window, text="")
appLabel.pack()

window.mainloop()