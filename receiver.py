import pyautogui as pg
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(1)

print("Waiting for a connection...")
client, addr = server.accept()
print("Connection from", addr) # When it receives a connection 


while True:
    data = client.recv(1024)
    if not data:
        break
    
    received_message = data.decode('utf-8') # Receive message
    print("Received:", received_message)
    rm = received_message
    if rm == 1:
        pg.keyDown("up")
    else:
        pg.keyUp("up")
    if rm == 2:
        pg.keyDown("down")
    else:
        pg.keyUp("down")
    if rm == 3:
        pg.keyDown("left")
    else:
        pg.keyUp("left")
    if rm == 4:
        pg.keyDown("right")
    else:
        pg.keyUp("right")

# Close the client connection
client.close()
