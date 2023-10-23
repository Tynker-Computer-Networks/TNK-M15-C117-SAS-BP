import socket
from  threading import Thread

from pynput.mouse import Button, Controller
from screeninfo import get_monitors
import autopy

SERVER = None
PORT = 8000
IP_ADDRESS = input("Enter your computer IP ADDR : ").strip()

# SA2: Create mouse object using controller class 


def recv_message(client_socket):
    # Access mouse as global
    
    while True:
        try:
            message = client_socket.recv(2048).decode()

            if(message):
                new_message  = eval(message)
                if(new_message["data"] == 'left_click'):
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                # Else check if 'right_click' is present at data key
                
                    # Press right button using mouse object
                    
                    # Release the right button 
                    
               
        except Exception as error:
            pass


def accept_connections():
    global SERVER

    while True:
        client_socket, addr = SERVER.accept()
        print(f"Connection established with {client_socket} : {addr}")

        thread_recv = Thread(target = recv_message, args=(client_socket,))
        thread_recv.start()


def setup():
    print("\n\t\t\t\t\t*** Welcome To Remote Mouse ***\n")

    global SERVER
    global PORT
    global IP_ADDRESS


    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")

    accept_connections()

setup()
