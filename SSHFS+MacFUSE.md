##Accessing the Pi Remotely: SSH and SSHFS



Unix systems (Mac, Linux) come with a utility called SSH, or Secure Shell, which allows you to easily connect to another SSH-enabled machine if you have its IP address and proper credentials.

###SSH: Secure Shell Access 

To SSH into your Pi, the most important piece of information you'll need is the Pi's IP address. To get this;
1. Open the terminal on your Pi and type `$ hostname -I` then press Enter. 
2. The window will simply return your IP address. 

**At this point, we will leave the Pi's native interface, so please write down this number.** 

On your own machine, we will set up SSH. 

1. First, make sure your computer and the Pi are connected to the **same wifi network**. 

2. If on a Mac, simply open the Terminal and type:

		ssh pi@PiIPAddress 

3. This attempts to log into the device at the address given with the user "**pi**." It will ask for a password. By default, this should be "**raspberry**."

Once the connection is established, you'll have command-line access to the Pi, just as if working from the Pi's own terminal. From here, you can easily install packages and run programs. However, if you don't have experience with SSH, it may be difficult to create new code and to visualize the Pi's environment. 

We have a solution. 


###SSHFS and FUSE: Mounting the Pi as a Drive

To access the Pi's filesystem via the OSX GUI, we will have to install two programs from the [OSX FUSE site](https://osxfuse.github.io/). 

1. Download and install **SSHFS (SSH Filse System)** and **FUSE for OSX.**

	*FUSE (Filesystem in User Space) allows us to manage a 	connected device as a locally mounted storage volume, similar 	to an external hard drive.*
	
2. Create a folder that you want to use a location to mount your Pi. Because you'll need to enter the file path later, we recommend creating a folder called "Mount" in your Home directory. 
	
	To find this directory on a Mac, do the following:
	a. Open a Finder window and navigate to something like "Documents."
	b. CMD+click on the name of the folder in the top bar of the window. 
	This will reveal the folders that the current window is nested within. One should have a 	small house icon next to it. This is your **home directory.** 
	c. Click on the home directory to open it in Finder. Create a new folder here named 	"mount."
	
3. Open your Mac's terminal and enter a command similar to the following:

		sshfs pi@PiIPAddress:// ~/mount -ovolname= mount
		
	The first "/" after the colon denotes the Pi's root folder, mounting the entire device. 
	
	The second unit of text, "~/mount," denotes the "mount" folder you've just made in your Mac's home folder. 

	The third unit, "-ovolname= mount" gives a new name to the second unit's location while the device is mounted, and is mostly of use to you as a user. 
	
4. Enter the password for your Raspberry Pi ("raspberry" by default)

5. Opening your "mount" folder, you should now see the file system of the Pi! The Pi's home folder is called **Pi**. You can now drag and drop files to this location, including new code written in an IDE on your Mac. 

 








 