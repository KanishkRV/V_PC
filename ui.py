import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print("Connected to server.")

    def send_command(self, command):
        self.client_socket.send(command.encode())
        response = self.client_socket.recv(1024).decode()
        print(response)

    def close(self):
        self.client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    HOST = "172.20.176.1"  # Change this to the server's IP address
    PORT = 12345        # Change this to the server's port

    client = Client(HOST, PORT)
    client.connect()

    while True:
        command = input("Enter command (start_vm, stop_vm, restart_vm, connect_usb <device>, disconnect_usb <device>, connect_display, disconnect_display, exit): ")
        if command.lower() == "exit":
            break
        client.send_command(command)

    client.close()
