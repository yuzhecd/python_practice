from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.5', 6789))
    server.listen(512)
    print('server is listening....')
    
    while True:
        client, addr = server.accept()
        print(str(addr) + 'is connected to the server')

        client.send(str(datetime.now()).encode('utf-8'))
        client.close()


if __name__ == '__main__':
    main()
