import tkinter as tk
def on_button_click():
    for index in appListbox.curselection():
        print(appListbox.get(index))

window = tk.Tk()

window.title("Exercice 1")
window.geometry("800x300")

langue_var = tk.StringVar()
keywords = ('Phishing', 'Malware', 'Firewall', 'Chiffrement', 'VPN')

keywords_variable = tk.Variable(value=keywords)

appListbox= tk.Listbox(window, listvariable=keywords_variable, heigh=5, selectmode="multiple")
appListbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)

appButton = tk.Button(window, text="Afficher",command=on_button_click)
appButton.pack(pady=10)

window.mainloop()