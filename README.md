A simple keylogger with the ability to exfiltrate keylogs from the client's device to the server's device using sockets.

Server-side script

- Creates a socket, then binds the host and the port to it.
- Listens for only one connection, as multi-threading is not applied.
- Opens or creates a file and appends the exfiltrated keylogs to the file.


Client-side script

- Creates a socket, then connects to the host IP address and port.
- Uses a keyboard listener from the pynput library.
- Sends each keystroke to the server-side device.
- Each keystroke is encoded into a bytes object for data exfiltration using sockets.
