Create a Socket and Connect to a Server
===================


In this activity, you will learn to create a socket and connect to a server specified by global variables (IP_ADDRESS and PORT).

<img src = "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10947183/Slide_17C.gif" width = "50%" height="auto" >

Follow the given steps to complete this activity:


Define the Server Setup Function
* Open the 'server.py' file.


* Define a setup() function.
~~~python
def setup():
~~~


* Access SERVER, PORT, IP_ADDRESS as global.
~~~python
    global SERVER
    global PORT
    global IP_ADDRESS
~~~




Use Try-Except Block


* Use the try block that attempts to create a socket and connect to the server.
~~~python
try:
    # Code for socket creation and connection
    return True


except:
    # Code to handle exceptions
    return False
~~~


Socket Creation and Connection


*  Create a new socket using the socket module inside the try block.
~~~python
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
~~~


* Connect the socket (SERVER) to the server specified by the IP_ADDRESS and the PORT. 
~~~python
SERVER.connect((IP_ADDRESS, PORT))
~~~


* Save and run the code to check the output.
