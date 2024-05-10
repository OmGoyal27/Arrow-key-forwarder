# Client script (run on the sending computer)
import socket
import keyboard as kb

ip_add = '192.168.1.13'  # IP address of the receiver's computer

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_add, 12345))

def send(message):
    global client
    client.sendall(message.encode('utf-8')) # Sends the message

while True:
    try:
        if kb.is_pressed("up"):
            send("1")
        else:
            send("0")
        
        if kb.is_pressed("down"):
            send("2")
        else:
            send("0")

        if kb.is_pressed("left"):
            send("3")
        else:
            send("0")

        if kb.is_pressed("right"):
            send("4")
        else:
            send("0")
    except KeyboardInterrupt:
        client.close()
        break

print("Goodbye")





