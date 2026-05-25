import socket

server = socket.socket()
server.bind(("localhost", 5050))
server.listen(5)

print("Server running on port 5050...")

while True:
    client, address = server.accept()
    print(f"Connection received from {address}")

    request = client.recv(4096).decode()
    print("\nRequest Received:\n")
    print(request)

    if "GET" in request:
        try:
            with open("index.html", "r") as file:
                content = file.read()

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n\r\n"
                + content
            )

        except FileNotFoundError:
            response = (
                "HTTP/1.1 404 Not Found\r\n\r\n"
                "File not found"
            )

    elif "POST" in request:
        body = request.split("\r\n\r\n", 1)[1]

        with open("upload.txt", "w") as file:
            file.write(body)

        response = (
            "HTTP/1.1 200 OK\r\n\r\n"
            "File Uploaded Successfully"
        )

    else:
        response = (
            "HTTP/1.1 400 Bad Request\r\n\r\n"
            "Invalid Request"
        )

    client.send(response.encode())
    client.close()
