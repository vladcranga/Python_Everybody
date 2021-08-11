from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
request = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(request)

end = False

while not end:
    data = sock.recv(512)
    if (len(data) < 1):
        end = True
    print(data.decode())

sock.close()
