# Keylogger with Exfiltration via Sockets

This project involves a keylogger that captures keystrokes on a client device and exfiltrates the key logs to a server using socket communication.

## Overview

### Server-Side Script

- **Purpose**: The server-side script listens for incoming connections from the client, receives key logs, and appends them to a specified log file.
- **Functionality**:
  - Sets up a TCP socket, and binds it to a designated host and port.
  - Listens for a single client connection (note: multi-threading is not implemented).
  - Opens or creates a file to store key logs and continuously appends the incoming data to this file.

### Client-Side Script

- **Purpose**: The client-side script captures keystrokes from the user's device and sends these logs to the server.
- **Functionality**:
  - Creates a TCP socket, then connects to the server's IP address and port.
  - Uses the `pynput` library to listen for keyboard events.
  - Encodes each keystroke into a bytes object and transmits it to the server.

## Instructions

1. **Running the Server-Side Script**:
   - Configure the host and port settings if needed.
   - Start the server-side script to begin listening for incoming connections.

2. **Running the Client-Side Script**:
   - Update the server IP address and port in the client-side script.
   - Execute the client-side script to log keystrokes and send them to the server.
