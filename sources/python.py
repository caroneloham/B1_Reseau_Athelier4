import tkinter as tk
from tkinter import ttk
import subprocess
import threading
import os
import shodan
script_commands = [
    "echo Déterminez si le serveur distant est accessible.",
    "echo Déterminez si le serveur distant est accessible. >> Analyse.txt",
    "ping -4 cisco.com",
    "ping -4 cisco.com >> Analyse.txt",
    "ping -6 cisco.com",
    "ping -6 cisco.com >> Analyse.txt",
    "echo Test V4",
    "echo Organismes principaux d'Internet",
    "echo Organismes principaux d'Internet >> Analyse.txt",
    "ping -4 www.afrinic.net",
    "ping -4 www.afrinic.net >> Analyse.txt",
    "ping -4 www.apnic.net",
    "ping -4 www.apnic.net >> Analyse.txt",
    "ping -4 www.ripe.net",
    "ping -4 www.ripe.net >> Analyse.txt",
    "ping -4 www.lacnic.net",
    "ping -4 www.lacnic.net >> Analyse.txt",
    "ping -4 www.arin.net",
    "ping -4 www.arin.net >> Analyse.txt",
    "echo Test V6",
    "ping -6 www.afrinic.net",
    "ping -6 www.afrinic.net >> Analyse.txt",
    "ping -6 www.apnic.net",
    "ping -6 www.apnic.net >> Analyse.txt",
    "ping -6 www.ripe.net",
    "ping -6 www.ripe.net >> Analyse.txt",
    "ping -6 www.lacnic.net",
    "ping -6 www.lacnic.net >> Analyse.txt",
    "ping -6 www.arin.net",
    "ping -6 www.arin.net >> Analyse.txt",
    "echo Suivre une route vers un serveur distant à l’aide de la commande Tracert",
    "echo Suivre une route vers un serveur distant à l’aide de la commande Tracert >> Analyse.txt",
    "tracert www.cisco.com",
    "tracert www.cisco.com >> Analyse.txt",
    "tracert peugeot.fr",
    "tracert peugeot.fr >> Analyse.txt",
    "tracert sfr.fr",
    "tracert sfr.fr >> Analyse.txt",
    "tracert cisco.fr",
    "tracert cisco.fr >> Analyse.txt",
    "tracert -h 5 google.com",
    "tracert -h 5 google.com >> Analyse.txt",
    "curl -s http://ping.eu/",
    "curl -s http://ping.eu/ >> Analyse.txt",
    "curl -s http://www.subnetonline.com/pages/network-tools/online-tracepath.php",
    "curl -s http://www.subnetonline.com/pages/network-tools/online-tracepath.php >> Analyse.txt",
    "curl -s https://www.root-me.org/",
    "curl -s https://www.root-me.org/ >> Analyse.txt",
    "pathping www.root-me.org",
    "pathping www.root-me.org >> Analyse.txt",
    "echo Afficher le fichier host 172.31.1.76 anissa",
    "echo Afficher le fichier host 172.31.1.76 anissa >> Analyse.txt",
    "ipcontype %windir%\\system32\\drivers\\etc\\hosts",
    "ipcontype %windir%\\system32\\drivers\\etc\\hosts >> Analyse.txt",
    "ipconfig /displaydns",
    "ipconfig /displaydns >> Analyse.txt",
    "ipconfig /flushdns",
    "ipconfig /flushdns >> Analyse.txt",
    "echo ARP",
    "echo ARP >> Analyse.txt",
    "arp -a",
    "arp -a >> Analyse.txt",
    "arp -d",
    "arp -s 192.168.1.100 00-aa-11-bb-22-cc",
    "arp -s 192.168.1.100 00-aa-11-bb-22-cc >> Analyse.txt",
    "arp -s 192.168.1.101 11-bb-22-cc-dd-ee",
    "arp -s 192.168.1.101 11-bb-22-cc-dd-ee >> Analyse.txt",
    "arp -s 192.168.1.102 22-cc-dd-ee-ff-00",
    "arp -s 192.168.1.102 22-cc-dd-ee-ff-00 >> Analyse.txt",
    "arp -s 192.168.1.103 33-dd-ee-ff-00-11",
    "arp -s 192.168.1.103 33-dd-ee-ff-00-11 >> Analyse.txt",
    "arp -s 192.168.1.104 44-ee-ff-00-11-22",
    "arp -s 192.168.1.104 44-ee-ff-00-11-22 >> Analyse.txt",
    "arp -a",
    "arp -a >> Analyse.txt",
    "echo Route",
    "echo Route >> Analyse.txt",
    "route print -4",
    "route print -4 >> Analyse.txt",
    "route print -6",
    "route print -6 >> Analyse.txt",
    "echo Netsh",
    "echo Netsh >> Analyse.txt",
    "netsh interface ipv4 show interfaces",
    "netsh interface ipv4 show interfaces >> Analyse.txt",
    "netsh interface show interface",
    "netsh interface show interface >> Analyse.txt",
    "netsh interface ipv4 show neighbors",
    "netsh interface ipv4 show neighbors >> Analyse.txt",
    "netsh int ip reset",
    "netsh int ip reset >> Analyse.txt",
    "systeminfo",
    "systeminfo >> Analyse.txt",
    "echo Netstat:",
    "echo Netstat: >> Analyse.txt",
    "netstat -an | Select-String \"TCP\" | Select-String \"LISTEN\"",
    "netstat -an | Select-String \"TCP\" | Select-String \"LISTEN\" >> Analyse.txt",
    "netstat -an | Select-String \"UDP\"",
    "netstat -an | Select-String \"UDP\" >> Analyse.txt",
    "netstat -e",
    "netstat -e >> Analyse.txt",
    "netstat -s",
    "netstat -s >> Analyse.txt",
    "netstat -b",
    "netstat -b >> Analyse.txt",
    "netstat -o",
    "netstat -o >> Analyse.txt",
    "echo Net session",
    "echo Net session >> Analyse.txt",
    "Net session",
    "Net session >> Analyse.txt",
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
                os.system("notepad.exe " + file_path)
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
open_button = tk.Button(root, text="Ouvrir le fichier texte", command=lambda: os.system("notepad.exe Analyse.txt"))
open_button.pack(pady=10)

# Étiquette pour afficher le statut des commandes
label = tk.Label(root, text="")
label.pack()

# Boucle principale de tkinter
root.mainloop()
