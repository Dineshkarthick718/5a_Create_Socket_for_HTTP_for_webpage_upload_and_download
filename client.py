import socket

client = socket.socket()
client.connect(("localhost", 5050))

print("1. Download Webpage")
print("2. Upload Content")
choice = input("Enter your choice: ")

if choice == "1":
    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client.send(request.encode())

    response = client.recv(4096).decode()
    print("\nServer Response:\n")
    print(response)

else:
    data = input("Enter text to upload: ")

    request = (
        "POST / HTTP/1.1\r\n"
        "Host: localhost\r\n"
        "Content-Type: text/plain\r\n\r\n"
        + data
    )

    client.send(request.encode())

    response = client.recv(4096).decode()
    print("\nServer Response:\n")
    print(response)

client.close()
