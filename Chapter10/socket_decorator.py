import socket


def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, "utf8"))
    client.close()