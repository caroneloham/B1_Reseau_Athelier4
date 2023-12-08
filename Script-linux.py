import tkinter as tk
from tkinter import ttk
import subprocess
import threading
import os

script_commands = [
    "echo Déterminez si le serveur distant est accessible.",
    "echo Déterminez si le serveur distant est accessible. >> Analyse.txt",
    "ping -c 4 cisco.com",
    "ping -c 4 cisco.com >> Analyse.txt",
    "ping6 -c 4 cisco.com",
    "ping6 -c 4 cisco.com >> Analyse.txt",
    "echo Test V4",
    "echo Organismes principaux d'Internet",
    "echo Organismes principaux d'Internet >> Analyse.txt",
    "ping -c 4 www.afrinic.net",
    "ping -c 4 www.afrinic.net >> Analyse.txt",
    "ping -c 4 www.apnic.net",
    "ping -c 4 www.apnic.net >> Analyse.txt",
    "ping -c 4 www.ripe.net",
    "ping -c 4 www.ripe.net >> Analyse.txt",
    "ping -c 4 www.lacnic.net",
    "ping -c 4 www.lacnic.net >> Analyse.txt",
    "ping -c 4 www.arin.net",
    "ping -c 4 www.arin.net >> Analyse.txt",
    "echo Test V6",
    "ping6 -c 4 www.afrinic.net",
    "ping6 -c 4 www.afrinic.net >> Analyse.txt",
    "ping6 -c 4 www.apnic.net",
    "ping6 -c 4 www.apnic.net >> Analyse.txt",
    "ping6 -c 4 www.ripe.net",
    "ping6 -c 4 www.ripe.net >> Analyse.txt",
    "ping6 -c 4 www.lacnic.net",
    "ping6 -c 4 www.lacnic.net >> Analyse.txt",
    "ping6 -c 4 www.arin.net",
    "ping6 -c 4 www.arin.net >> Analyse.txt",
    "echo Suivre une route vers un serveur distant à l’aide de la commande Tracert",
    "echo Suivre une route vers un serveur distant à l’aide de la commande Tracert >> Analyse.txt",
    "traceroute www.cisco.com",  # Utilisation de traceroute pour Linux
    "traceroute www.cisco.com >> Analyse.txt",
    "traceroute peugeot.fr",
    "traceroute peugeot.fr >> Analyse.txt",
    "traceroute sfr.fr",
    "traceroute sfr.fr >> Analyse.txt",
    "traceroute cisco.fr",
    "traceroute cisco.fr >> Analyse.txt",
    "traceroute -m 5 google.com",  # Utilisation de l'option -m pour spécifier le nombre maximal de sauts
    "traceroute -m 5 google.com >> Analyse.txt",
    "curl -s http://ping.eu/",
    "curl -s http://ping.eu/ >> Analyse.txt",
    "curl -s http://www.subnetonline.com/pages/network-tools/online-tracepath.php",
    "curl -s http://www.subnetonline.com/pages/network-tools/online-tracepath.php >> Analyse.txt",
    "curl -s https://www.root-me.org/",
    "curl -s https://www.root-me.org/ >> Analyse.txt",
    "ip route get 172.31.1.76",  # Utilisation de la commande ip pour afficher le chemin du paquet
    "ip route get 172.31.1.76 >> Analyse.txt",
    "ip neigh show",
    "ip neigh show >> Analyse.txt",
    "ip route",  # Affiche la table de routage
    "ip route >> Analyse.txt",
    "ip link show",
    "ip link show >> Analyse.txt",
    "ip addr show",
    "ip addr show >> Analyse.txt",
    "ip link set dev enp0s3 down",  # Exemple de désactivation de l'interface (adapté à votre configuration)
    "ip link set dev enp0s3 up",  # Exemple d'activation de l'interface (adapté à votre configuration)
    "echo Afficher le fichier host 172.31.1.76 anissa",
    "echo Afficher le fichier host 172.31.1.76 anissa >> Analyse.txt",
    "cat /etc/hosts | grep 172.31.1.76 anissa",  # Utilisation de cat et grep pour afficher la ligne correspondante
    "cat /etc/hosts | grep 172.31.1.76 anissa >> Analyse.txt",
    "ip route show",  # Affiche la table de routage
    "ip route show >> Analyse.txt",
    "ip -4 route show",  # Affiche la table de routage IPv4
    "ip -4 route show >> Analyse.txt",
    "ip -6 route show",  # Affiche la table de routage IPv6
    "ip -6 route show >> Analyse.txt",
    "ip neigh",  # Affiche la table ARP
    "ip neigh >> Analyse.txt",
    "ip -s neigh flush all",  # Vide la table ARP
    "ip -s neigh flush all >> Analyse.txt",
    "echo Netstat:",
    "echo Netstat: >> Analyse.txt",
    "netstat -tan | grep LISTEN",
    "netstat -tan | grep LISTEN >> Analyse.txt",
    "netstat -uan",
    "netstat -uan >> Analyse.txt",
    "netstat -s",
    "netstat -s >> Analyse.txt",
    "netstat -i",
    "netstat -i >> Analyse.txt",
    "netstat -p",
    "netstat -p >> Analyse.txt",
    "echo Net session",
    "echo Net session >> Analyse.txt",
    "ss -s",  # Affiche les statistiques du socket
    "ss -s >> Analyse.txt",
]

# Calcul du nombre total de commandes
total_commands = len(script_commands)

# Fonction pour exécuter les commandes
def run_commands():
    # Fonction pour exécuter les commandes en temps réel
    def execute_commands():
        try:
            for index, command in enumerate(script_commands, start=1):
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
                for line in process.stdout:
                    script_output_text.insert(tk.END, line)  # Affiche la sortie des commandes dans le widget Text
                    script_output_text.see(tk.END)  # Fait défiler automatiquement le widget Text pour afficher les nouvelles lignes
                process.communicate()
                # Calcule le pourcentage d'avancement et met à jour la barre de progression
                progress_percent = int((index / total_commands) * 100)
                progress_bar['value'] = progress_percent
                root.update_idletasks()
            return True
        except Exception as e:
            print("Erreur lors de l'exécution des commandes :", e)
            return False

    # Désactive le bouton pendant l'exécution des commandes
    run_button.config(state=tk.DISABLED)

    # Exécute les commandes dans un thread
    def run_commands_thread():
        if execute_commands():
            label.config(text="Les commandes ont été exécutées avec succès!")
            # Ouvre automatiquement le fichier "Analyse.txt" s'il existe
            file_path = os.path.join(os.path.dirname(__file__), "Analyse.txt")
            if os.path.exists(file_path):
                os.system("gedit " + file_path)  # Utilisation de gedit pour ouvrir le fichier texte
        else:
            label.config(text="Une erreur s'est produite lors de l'exécution des commandes.")

        # Réactive le bouton après l'exécution des commandes
        run_button.config(state=tk.NORMAL)
        progress_bar['value'] = 0  # Réinitialise la barre de progression

    script_thread = threading.Thread(target=run_commands_thread)
    script_thread.start()

# Crée la fenêtre principale
root = tk.Tk()
root.title("TP4_SCRIPT_DROGUE")
root.geometry("400x400")

icone_path = "data/serveur.ico"
root.iconbitmap(default=icone_path)

# Crée un cadre pour aligner les éléments au milieu
middle_frame = tk.Frame(root)
middle_frame.pack(fill=tk.BOTH, expand=True)

# Bouton pour exécuter les commandes
run_button = tk.Button(middle_frame, text="Exécuter les commandes", command=run_commands)
run_button.pack(pady=10)

# Barre de progression
progress_bar = ttk.Progressbar(middle_frame, mode="determinate", maximum=100)
progress_bar.pack(pady=10)

# Widget Text pour afficher la sortie des commandes en temps réel
script_output_text = tk.Text(middle_frame, wrap=tk.WORD)
script_output_text.pack(fill=tk.BOTH, expand=True)

# Bouton pour ouvrir le fichier texte
open_button = tk.Button(root, text="Ouvrir le fichier texte", command=lambda: os.system("gedit Analyse.txt"))
open_button.pack(pady=10)

# Étiquette pour afficher le statut des commandes
label = tk.Label(root, text="")
label.pack()

# Boucle principale de tkinter
root.mainloop()
