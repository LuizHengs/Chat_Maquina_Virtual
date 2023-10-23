import socket
import threading
import customtkinter as ctk

SERVER_PORT = 8000
BUFFER = 1024

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1280x720")
        self.textbox = ctk.CTkTextbox(master=self, width=480, height=480, corner_radius=0)
        self.textbox.pack()

        self.start_server()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', SERVER_PORT))
        self.server_socket.listen(1)
        self.textbox.insert("end", "Waiting for a client to connect...\n")

        self.accept_client()

    def accept_client(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.textbox.insert("end", f"Client {client_address[0]} connected.\n")
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        while True:
            rec_message = client_socket.recv(BUFFER).decode("utf8")
            print(f'Client: {rec_message}')
            if not rec_message:
                break

            self.textbox.insert("end", f'Client: {rec_message}\n')

            if rec_message == "sair":
                self.textbox.insert("end", "Client terminated the connection.\n")
                break

            response = input("Server: ")
            client_socket.send(bytes(response, "utf8"))

        client_socket.close()

if __name__ == '__main__':
    app = App()
    app.mainloop()
