import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('192.168.5.38', 8000)

# Send a message to the server
message = 'Hello, server!'
client_socket.sendto(message.encode(), server_address)

# Receive the server's response
response, server_address = client_socket.recvfrom(1024)
print('Server response:', response.decode())

# Close the socket
client_socket.close()
