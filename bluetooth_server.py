import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

print("Waiting for connection on RFCOMM...")

client_sock, address = server_sock.accept()
print(f"Accepted connection from {address}")

try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        print("Received:", data.decode())
except OSError:
    pass

print("Disconnected.")
client_sock.close()
server_sock.close()

