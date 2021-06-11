# PYNQAXII2CMaster

To use this code you will need:

* A ZYNQ TUL-2 board
* A https://smile.amazon.com/SunFounder-Serial-Module-Display-Arduino/dp/B019K5X53O/ref=sr_1_2_sspa?dchild=1&keywords=I2C+lcd&qid=1623374997&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOUlRS0k2NFVLTTJSJmVuY3J5cHRlZElkPUEwNDk2ODEzOVJPQ0dSQVNXUE1VJmVuY3J5cHRlZEFkSWQ9QTA2ODU0NjUzSFNMNVJNWFlCU1RDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== Display Board 
* A ZYNQ image which uses the axi_iic_0 module and maps it to the ZYNQ Processing system. 

You will also need to run VCC, GND, SCL and SCA from the ZYNQ to the Display. You can then use
the DisplayDriver to drive out a message to the I2C. 
