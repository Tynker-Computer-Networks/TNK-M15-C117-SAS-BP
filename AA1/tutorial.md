Debug the Mouse Click
=================


In this activity, you will identify why the right and left clicks are not working and debug the code.

<img src ="https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10926122/Slide_71.gif" width = "50%" height = "auto">

Follow the given steps to complete this activity:


* Run the code to identify why the right and left clicks are not working.


* The if condition compares the entire new_message dictionary to the string 'left_click'. However, it seems that the expected structure of the message is a dictionary with a key 'data' that holds the information about the click.


* Open the file `server.py`.


* Change the if statement of the left click to rectify new_message for access to the value stored in the new_message["key"], and check if it contains the string 'left_click'.
~~~python
if(new_message["data"] == 'left_click'):
~~~




* Change the elif statement for the mouse right click simulation to rectify new_message for access to the value stored in new_message["key"], and if it contains the string 'left_click'.
~~~python
elif(new_message["data"] == 'right_click'):
~~~


* Save and run the code to check the output.
