# 5a_Create_Socket_for_HTTP_for_webpage_upload_and_download

## AIM
To write a Python program for socket communication using HTTP protocol for webpage upload and download.

---

## ALGORITHM

1. Start the server program.
2. Create a socket using Python socket module.
3. Bind the server to localhost and port number 5050.
4. Listen for incoming client requests.
5. Create a client socket and connect to the server.
6. Send HTTP GET request to download webpage.
7. Send HTTP POST request to upload data.
8. Server processes the request and sends response.
9. Display the response on client side.
10. Stop the program.

---

## PROGRAM

### Client Program (`client.py`)

```python
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
```

---

### Server Program (`server.py`)

```python
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
```

---

### HTML Webpage (`index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Socket HTTP Demo</title>
</head>
<body>
    <h1>HTTP Webpage Upload and Download</h1>
    <p>This webpage is served using Python socket programming.</p>
</body>
</html>
```

---

## OUTPUT

### Download Operation

- Client sends HTTP GET request.
- Server returns the content of `index.html`.
- Webpage content is displayed on the client terminal.

### Upload Operation

- Client sends HTTP POST request with text data.
- Server stores the data in `upload.txt`.
- Success message is displayed.

---

## RESULT
Thus the Python program for socket communication using HTTP protocol for webpage upload and download was created and executed successfully.
