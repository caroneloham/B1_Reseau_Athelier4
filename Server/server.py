import socket
import threading
import tkinter as tk
from tkinter import ttk, messagebox


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}

        self.root = tk.Tk()
        self.root.title("Server")

        self.client_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.client_listbox.pack(pady=10)

        self.execute_button = ttk.Button(self.root, text="Exécuter", command=self.execute_script)
        self.execute_button.pack(pady=10)

        self.update_button = ttk.Button(self.root, text="Actualiser", command=self.update_client_list)
        self.update_button.pack(pady=10)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(10)

        self.accept_thread = threading.Thread(target=self.accept_connections)
        self.accept_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def accept_connections(self):
        while True:
            try:
                client, addr = self.server_socket.accept()
                self.clients[addr] = {"socket": client, "name": ""}

                threading.Thread(target=self.handle_client, args=(client, addr)).start()
            except Exception as e:
                print(f"Erreur lors de l'acceptation de la connexion : {e}")

    def handle_client(self, client, addr):
        try:
            name = client.recv(1024).decode('utf-8')
            self.clients[addr]["name"] = name
            self.client_listbox.insert(tk.END, f"{name} - {addr[0]}")

            while True:
                message = client.recv(1024).decode('utf-8')
                if not message:
                    break

                # Ajoutez ici le code pour interpréter d'autres messages et agir en conséquence.
        except (socket.error, OSError):
            self.remove_client(addr)

    def remove_client(self, addr):
        if addr in self.clients:
            name = self.clients[addr]["name"]
            self.client_listbox.delete(tk.END, f"{name} - {addr[0]}")
            self.clients.pop(addr)

    def update_client_list(self):
        self.client_listbox.delete(0, tk.END)
        for addr, client_info in self.clients.items():
            name = client_info["name"]
            self.client_listbox.insert(tk.END, f"{name} - {addr[0]}")

    def execute_script(self):
        selected_index = self.client_listbox.curselection()
        if selected_index:
            selected_client = self.client_listbox.get(selected_index)
            selected_addr = selected_client.split(" - ")[1]
            selected_socket = self.clients[selected_addr]["socket"]

            try:
                selected_socket.send("script".encode('utf-8'))
            except socket.error:
                self.remove_client(selected_addr)
                messagebox.showerror("Erreur", "La connexion a été interrompue.")

    def on_closing(self):
        self.server_socket.close()
        self.root.destroy()


if __name__ == "__main__":
    server = Server("127.0.0.1", 12345)
