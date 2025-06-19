import tkinter as tk
def handle_item_select(event):
    selected_indices = appListbox.curselection()
    for indice in selected_indices:
        if indice == 0:
            appText.delete(1.0,tk.END)
            appText.insert(1.0, "Aucune restriction")
        elif indice == 1:
            appText.delete(1.0,tk.END)
            appText.insert(1.0,"Accès restreint au personnel autorisé")
        else:
            appText.delete(1.0,tk.END)
            appText.insert(1.0,"Accès limité, autorisation spéciale requise")

window = tk.Tk()
window.title("Exercice 2")
window.geometry("800x300")
appListbox = tk.Listbox(window, heigh = 3)
types_classements =["Public","Confidentiel","Très Secret"]
for classement in types_classements:
    appListbox.insert(tk.END,classement)
appListbox.pack()
appText = tk.Text(window, height=1, width=45)
appText.pack()
appListbox.bind('<<ListboxSelect>>', handle_item_select)

# lancer mon application
window.mainloop()