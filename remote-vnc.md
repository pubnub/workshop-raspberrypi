# Remote Access using VNC

Remote access to the Pi's graphical interface, viewed in a window on another computer.

Make sure that your Pi is running (power cable is attached), and Wi-Fi is connected. You can disconnect a monitor, keyboard, and mouse.


## VNC Server on Pi

On your computer, SSH to your Pi:

`you@Mac $ ssh 10.96.70.1 -l pi` // use your Pi's IP address

(Or you can operate the followings directly on Pi.)

Install the TightVNC package

`pi@raspberrypi ~ $ sudo apt-get install tightvncserver`

Run TightVNC Server

`pi@raspberrypi ~ $ tightvncserver`

This will prompt you to enter a password and an optional view-only password.

## VNC Client on Computer

1. Download [VNC Client](http://www.realvnc.com/download/vnc/latest) and install.

2. Enter the Pi's IP address, followed by the screen number `:1`. Then click **Connect**.

![image](images/vnc-viewer.png)

3. At the Unencrypted Connection prompt, click **Continue**

4. Now you should get the Rapberry Pi desktop!

![image](images/vnc-pi.png)


## Reference

[VNC (Virtual Network Computing)](http://www.raspberrypi.org/documentation/remote-access/vnc/README.md) by RaspberryPi.org 
