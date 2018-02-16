import socket


# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the web server on port 8888 - the normal http port
s.connect(("dialectid.qcri.org", 8888))
