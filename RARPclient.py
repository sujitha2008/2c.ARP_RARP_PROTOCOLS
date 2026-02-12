import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9090))

while True:
    mac = input("Enter MAC address (or 'exit' to stop): ")

    if mac.lower() == "exit":
        break

    client.send(mac.encode())
    ip = client.recv(1024).decode()
    print("IP Address:", ip)

client.close()
