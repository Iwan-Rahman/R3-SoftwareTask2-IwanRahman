import socket

# Server Information
HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432

# Rover Movement
wheels = ['', '', '', '']
wheels_direction = ['f', 'f', 'f', 'f']
wheels_speed = 0


# Rover Movement
def update_movement():
    global wheels
    for i in range(0, 4):
        wheels[i] = wheels_direction[i] + str(wheels_speed)
    print(wheels)


def direction_input(key):
    global wheels_direction

    if key == 'w':  # Going Forward
        wheels_direction = ['f', 'f', 'f', 'f']
    elif key == 's':  # Going Reverse
        wheels_direction = ['r', 'r', 'r', 'r']
    elif key == 'a':  # Turning Left
        wheels_direction = ['r', 'r', 'f', 'f']
    elif key == 'd':  # Turning Right
        wheels_direction = ['f', 'f', 'r', 'r']
    return wheels_direction


def speed_input(key):
    global wheels_speed
    if key == '0':  # Stops Rover
        wheels_speed = 0
    elif key == '1':  # Lowest Speed
        wheels_speed = 51
    elif key == '2':  # Lower Speed
        wheels_speed = 102
    elif key == '3':  # Medium Speed
        wheels_speed = 153
    elif key == '4':  # High Speed
        wheels_speed = 204
    elif key == '5':  # Highest Speed
        wheels_speed = 255
    return wheels_speed


def output_message(data):
    # Store data as a string
    key = data.decode()
    key = key.replace("'", "")

    # Updates and Stores Wheel Direction or Speed
    direction_input(key)
    speed_input(key)

    # Checks for valid input
    if key != 'w' and key != 'a' and key != 's' and key != 'd':
        if key != '0' and key != '1' and key != '2' and key != '3' and key != '4' and key != '5':
            print("Type wasd to control the direction of the rover. \n Type 12345 to control the speed of the rover")
    pass


# Server Setup
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    count = 0
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('connected by', addr)
        while True:
            data = conn.recv(1024)
            output_message(data)
            update_movement()
            conn.sendall(data)
