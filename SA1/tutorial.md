Create the Mouse Object
===========================


In this activity, you will learn to create a mouse object and enable right click functionality.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10926089/Slide_25.gif" width = "50%" height = "auto">

https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10926089/Slide_25.gif

Follow the given steps to complete this activity:


Import the required libraries
* Open the `server.py` file.


* Import the button and controller classes from the pynput.mouse module.
~~~python
from pynput.mouse import Button, Controller
~~~


* Import the get_monitors function from the screeninfo module.
~~~python
from screeninfo import get_monitors
~~~


* Import the autopy module.
~~~python
import autopy
~~~


Create a mouse controller object
* Open the `client.py` file.


* Create a mouse object using the controller class.
~~~python
mouse = Controller()
~~~


* Define the recv_message() function that continuously receives messages from a client socket. In the function, access the mouse controller object as global.
~~~python
def recv_message(client_socket):
    global mouse
~~~




Enable mouse right click functionality


* Add an else statement to check if the data key contains the string 'right_click' and enable the simulation for mouse right click.
~~~python
elif(new_message["data"] == 'right_click'):
~~~


* Simulate the pressing of the right mouse button.
~~~python
mouse.press(Button.right)
~~~


* Simulate the release of the right mouse button.
~~~python
mouse.release(Button.right)
~~~


* Save and run the code to check the output.
