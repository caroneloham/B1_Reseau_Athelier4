import socket
import subprocess
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
import os

class Client:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.client_socket.send(name.encode('utf-8'))

        self.root = tk.Tk()
        self.root.title(f"Client - {self.name}")

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break

                if message == "script":
                    self.execute_script()

            except (socket.error, OSError):
                messagebox.showerror("Erreur", "La connexion a été interrompue.")
                break

    def execute_script(self):
        try:
            script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "script.bat")
            subprocess.run([script_path], shell=True)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'exécution du script : {e}")

    def on_closing(self):
        self.client_socket.close()
        self.root.destroy()

if __name__ == "__main__":
    name = simpledialog.askstring("Nom", "Entrez votre prénom:")
    client = Client("127.0.0.1", 12345, name)
