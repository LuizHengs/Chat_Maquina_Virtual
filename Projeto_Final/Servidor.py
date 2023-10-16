import socket
import sys

SERVER_IP = ''
SERVER_POT = 8000
BUFFER = 1024

def bind_to_the_server():

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server = (SERVER_IP, SERVER_POT)
    connection.bind(socket_server)
    connection.listen(1)

    return connection

def client_confirmation(connection):

    connection, ip_cliente = connection.accept()
    print(f"O cliente com endereço de IP f{ip_cliente[0]} aceitou.")
    return connection, ip_cliente

def close_connection(connection):

    print("Terminando a conexao e saindo do programa...")
    connection.close()

def listening (connection, ip_cliente):
    print("Começando o chat. Esperando por uma mensagem...")

    while True:
        rec_mensagem = connection.recv(BUFFER).decode("utf8")

        if rec_mensagem != "":
            print(f"\nCliente {ip_cliente[0]}: {rec_mensagem}")
            if rec_mensagem == "sair":
                print("O lado do cliente terminou a conexao. Digite 'sair' para terminar a conexao")

        sending_mensagem = input("Servidor: ")

        if sending_mensagem != "":
            connection.send(bytes(sending_mensagem, "utf8"))
            if sending_mensagem == "sair":
                break

    print("Saindo...")
    close_connection(connection)



if __name__ == '__main__':
    conexao_atual = bind_to_the_server()
    conexao_aceita, ip_cliente = client_confirmation(conexao_atual)
    listening(conexao_aceita, ip_cliente)

    sys.exit()

