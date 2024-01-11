Debug the Trackpad
==============


In this activity, you will learn to debug the code to check why the mouse trackpad is not working correctly by calculating the mouse position based on the received message.

<img src ="https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10926122/Slide_71.gif" width = "50%" height = "auto">

Follow the given steps to complete this activity:


* Run the code to check whether the mouse trackpad is functioning correctly or not.


* The code has an issue with how the mouse position is being calculated based on the received message. 


* Open the file `server.py`.


* Switch the assignment of ypos and xpos in the given code to reflect a more accurate calculation for the mouse position based on the received message. 


~~~python
ypos = new_message["data"][0] * screen_width
xpos = screen_height * (1 - (new_message["data"][1] - 0.2) / 0.6 )
~~~
* Save and run the code to check the output.
