import socket
import sys

SERVER_POT = 8000
BUFFER = 1024

def connecting():

    value = input("Coloque o endereço de IP para começar a comunicaçao: ")
    confirmation = input(f"\nO endereço de destino e {value}. E isso mesmo?\n ('s' ou 'n'): ")

    confirmation = (False if confirmation == 'n' else True)
    if confirmation is False:
        print("Saindo...")
        sys.exit()

    return start_connection(value)

def checking_ip_address (ip_address):
    if len(ip_address) == 9 and ip_address is not None:
        return True
    print("Terminando o programa... cheque se o endereço de IP foi corrigido!")
    sys.exit()

def start_connection(ip_address):

    print("Tentando se conectar ao servidor...")
    checking_ip_address(ip_address)
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket.SOCK_STREAM eh para conexao TCP. Para realizar UDP, use socket.SOCK_DGRAM
    try:
        destino = (ip_address,SERVER_POT)
        connection.connect(destino)
    except ConnectionError as erro:
        print("Conexao recusada. "
              f"Tipo do erro: {type(erro)}")

    return connection

def close_connection(connection):
    print("Terminando a conexao UDP...")
    connection.close()

def conversation(connection):
    print("Começando o chat! Para sair, escreva: 'sair'")

    while True:
        mensagem = input("\nVoce: ")

        if mensagem != "":
            connection.send(bytes(mensagem, "utf8"))
            if mensagem == "sair":
                break

        rec_mensagem = connection.recv(BUFFER).decode("utf8")

        if rec_mensagem != "":
            print(f"Servidor: {rec_mensagem}")
            if rec_mensagem == "sair":
                print("O lado do servidor terminou a conexao. Informe 'sair' para terminar a conexao")

    print("Saindo...")
    close_connection(connection)

if __name__ == '__main__':
    print("Bem vindo ao chat com comunicaçao socket UDP!")

    conexao = connecting()
    conversation(conexao)

    try:
        conexao.close()
    except ConnectionError as erro:
        print("A conexao UDP chegou ao fim")




