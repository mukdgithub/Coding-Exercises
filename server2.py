import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('192.168.5.38', 8000)

# Bind the socket to the server address and port
server_socket.bind(server_address)

print('Server is listening on {}:{}'.format(*server_address))

# Receive data from the client
data, client_address = server_socket.recvfrom(1024)
print('Received message:', data.decode())

# Send a response back to the client
response = 'Message received: {}'.format(data.decode())
server_socket.sendto(response.encode(), client_address)

# Close the socket
server_socket.close()
