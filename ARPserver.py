import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(1)

print("ARP Server is running...")
print("Waiting for client connection...\n")

conn, addr = server.accept()
print("Connected to client:", addr)
arp_table = {
    "192.168.1.1": "AA:BB:CC:DD:EE:01",
    "192.168.1.2": "AA:BB:CC:DD:EE:02",
    "192.168.1.3": "AA:BB:CC:DD:EE:03"
}

while True:
    ip = conn.recv(1024).decode()
    if not ip:
        break

    print("ARP Request for IP:", ip)

    mac = arp_table.get(ip, "IP address not found")
    conn.send(mac.encode())

conn.close()
server.close()

