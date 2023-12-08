import os
import tkinter as tk
from tkinter import messagebox
def ajouter_entree_hosts():
    nom = entry_nom.get()
    ip = entry_ip.get()

    if not nom or not ip:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

    try:
        with open(hosts_path, 'a') as hosts_file:
            hosts_file.write(f'{ip}\t{nom}\n')
        messagebox.showinfo("Succès", f"L'entrée {nom} a été ajoutée au fichier hosts.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")

fenetre = tk.Tk()
fenetre.title("Ajouter une entrée dans le fichier hosts")
label_nom = tk.Label(fenetre, text="Nom:")
entry_nom = tk.Entry(fenetre)
label_ip = tk.Label(fenetre, text="Adresse IP:")
entry_ip = tk.Entry(fenetre)
bouton_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_entree_hosts)
label_nom.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nom.grid(row=0, column=1, padx=10, pady=5)
label_ip.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_ip.grid(row=1, column=1, padx=10, pady=5)
bouton_ajouter.grid(row=2, column=0, columnspan=2, pady=10)
fenetre.mainloop()
