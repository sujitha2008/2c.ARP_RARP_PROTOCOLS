import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))

while True:
    ip = input("Enter IP address (or 'exit' to stop): ")

    if ip.lower() == "exit":
        break

    client.send(ip.encode())
    mac = client.recv(1024).decode()
    print("MAC Address:", mac)

client.close()