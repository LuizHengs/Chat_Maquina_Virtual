import socket
import sys

SERVER_IP = ''
SERVER_POT = 8000
BUFFER = 1024

def bind_to_the_server():

    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server = (SERVER_IP, SERVER_POT)
    connection.bind(socket_server)
    #connection.listen(1)

    return connection


def close_connection(connection):

    print("Terminando a conexao e saindo do programa...")
    connection.close()

def listening (connection):
    print("Começando o chat. Esperando por uma mensagem...")

    while True:
        rec_mensagem, clienteAddress = connection.recvfrom(BUFFER)

        if rec_mensagem != "":
            print(f"\nCliente: {rec_mensagem.decode()}")
            if rec_mensagem.decode() == "sair":
                print("O lado do cliente terminou a conexao. Digite 'sair' para terminar a conexao")

        sending_mensagem = input("Servidor: ")

        if sending_mensagem != "":
            connection.sendto(sending_mensagem.encode(), clienteAddress)
            if sending_mensagem == "sair":
                break

    print("Saindo...")
    close_connection(connection)



if __name__ == '__main__':
    conexao_atual = bind_to_the_server()
    listening(conexao_atual)

    sys.exit()

