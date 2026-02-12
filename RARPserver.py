import socket

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9090))
server.listen(1)

print("RARP Server is running...")
print("Waiting for client connection...\n")

conn, addr = server.accept()
print("Connected to client:", addr)

# Simulated RARP table (MAC → IP)
rarp_table = {
    "AA:BB:CC:DD:EE:01": "192.168.1.1",
    "AA:BB:CC:DD:EE:02": "192.168.1.2",
    "AA:BB:CC:DD:EE:03": "192.168.1.3"
}

while True:
    mac = conn.recv(1024).decode()
    if not mac:
        break

    print("RARP Request for MAC:", mac)

    ip = rarp_table.get(mac, "MAC address not found")
    conn.send(ip.encode())

conn.close()
server.close()
