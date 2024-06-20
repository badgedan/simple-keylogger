import socket
try:
    print("Creating socket..")
    s=socket.socket()
    host=""
    port=12345
except socket.error as msg:
    print("Error occoured while creating the socket "+str(msg))

try:
    print("Binding port: "+str(port))
    s.bind((host,port))
    s.listen(10)
except socket.error as msg:
    print("Error occourd while binding the socket "+str(msg))


output_path="" # insert the full path of the output file

while True: 
        c, addr = s.accept()
        print("Received a connection from: " + str(addr))
        with open(str(output_path), "a") as fo:
            while True:
                data = c.recv(1024).decode()
                if not data:
                    print("No data received. Closing connection.")
                    c.close()
                    break
                print("Received data: " + str(data))
                fo.write(data)
