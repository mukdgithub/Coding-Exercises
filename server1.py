import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('192.168.5.38', 8000)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print('Server is listening on {}:{}'.format(*server_address))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print('Connected to client:', client_address)

# Receive data from the client
data = client_socket.recv(1024).decode()
print('Received message:', data)

# Send a response back to the client
response = 'Message received: {}'.format(data)
client_socket.sendall(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
