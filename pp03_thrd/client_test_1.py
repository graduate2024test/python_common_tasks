import socket

SERVER = "127.0.0.1"

PORT = 40900

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))

client.sendall(bytes("This is from Client", 'utf-8'))

while True:
	in_data = client.recv(1024)
	print("From Server: ", in_data.decode())
	
	out_data = input("Enter the msg to server: ")
	
	client.sendall(bytes(out_data, 'utf-8'))
	if out_data == 'bye':
		break
		
client.close()
