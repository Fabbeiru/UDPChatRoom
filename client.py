import socket
import threading
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("localhost", random.randint(0000, 1000)))

name = input("Nickname: ")


def receive():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass


t = threading.Thread(target=receive)
t.start()

client.sendto(f"SIGNUP_TAG: {name}".encode(), ("localhost", 1313))

while True:
    message = input("")
    if message == "!q":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), ("localhost", 1313))
