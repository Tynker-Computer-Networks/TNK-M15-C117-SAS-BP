Control the Mouse Position
===========================


In this activity, you will learn to calculate the screen width and height to control the mouse pointer remotely on the screen.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10926089/Slide_25.gif" width = "50%" height = "auto">


Follow the given steps to complete this activity:


Create screen_width variable
* Open the `server.py` file.


*  Create a screen_width variable with none value.
~~~python
screen_width = None
~~~


Access screen_width as global


* Access screen_width as global.
~~~python
global screen_height, screen_width
~~~


Fetch the Screen Width


*   Fetch the width of a screen and store that value in the variable screen_width using monitor info. 
~~~python
screen_width = monitor.width
~~~


Calculate the x-position of the mouse


*  Calculate the x position for the mouse pointer by multiplying the first element of new_message["data"] by the screen width.
~~~python
xpos = new_message["data"][0] * screen_width
~~~


*  Change the x coordinate of the mouse position from 10 to int(xpos) to update the mouse cursor's position using the calculated x-coordinate (xpos) and y-coordinate (ypos).


~~~python
#mouse.position = (10, int(ypos))


mouse.position = (int(xpos), int(ypos))
~~~


* Save and run the code to check the output.
