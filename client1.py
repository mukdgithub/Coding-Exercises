import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('192.168.5.38', 8000)

# Connect to the server
client_socket.connect(server_address)
print('Connected to server:', server_address)

# Send a message to the server
message = 'Hello, server!'
client_socket.sendall(message.encode())

# Receive the server's response
response = client_socket.recv(1024).decode()
print('Server response:', response)

# Close the connection
client_socket.close()
