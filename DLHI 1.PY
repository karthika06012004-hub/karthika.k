import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("your Computer Name:",hostname)
print("your IP address:",ip_address)
