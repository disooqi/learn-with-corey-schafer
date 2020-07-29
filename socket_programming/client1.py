import socket
import  time
HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b"Hello, world")
#     data = s.recv(1024)
#
# print("Received", repr(data))



PORT = 9600  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # data = s.recv(1024)
    # print("Received", repr(data))
    s.sendall(b"Hello, world 7")
    data = s.recv(1024)
    s.sendall(b"Hello, world 7")
    data = s.recv(1024)
    print("Received", repr(data))
    # data = s.recv(1024)
