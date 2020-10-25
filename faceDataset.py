#!/usr/bin/python3

# import the necessary packages
from __future__ import print_function
from faceclass.faceapp import FaceApp
from imutils.video import VideoStream
import time
from tkinter import *
from tkinter import ttk
import cv2
import os

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-o", "--output", required=True,
#	help="path to output directory to store snapshots")
#ap.add_argument("-p", "--picamera", type=int, default=-1,
#	help="whether or not the Raspberry Pi camera should be used")
#args = vars(ap.parse_args())

secondary_directory=""
database_directory=""
current_directory=""
passValue=0
videoFlag=0

def database(*args):
    global secondary_directory
    global database_directory
    global current_directory
    global videoFlag
    try:
        value = (enterString.get())
        if(value==""):
        	showValue.set("No Folder Created Try Again!!!")
        else:
            showValue.set(value+" Folder Created")
            videoFlag=1
        	
        

        
        
        current_directory = os.getcwd()
        database_directory = os.path.join(current_directory, r'dataset')
        
        if not os.path.exists(database_directory):
            os.makedirs(database_directory)
        secondary_directory = os.path.join(database_directory, value)
        if not os.path.exists(secondary_directory):
            os.makedirs(secondary_directory)
        
          
    except ValueError:
    	pass


def videoStream(*args):
    global passValue
    global videoFlag
    try:
        if (videoFlag==1):
            passValue=1
        else:
            passValue=0
        root.destroy()

    except ValueError:
        pass
root = Tk()
root.title("Database Creation")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



enterString = StringVar()
showValue = StringVar()

folder_entry = ttk.Entry(mainframe, width=7, textvariable=enterString)
folder_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=showValue).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Create", command=database).grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Enter the person name to create folder ").grid(column=2, row=1, sticky=E)
ttk.Label(mainframe, text="NOTE: Without creating a folder capturing will not start").grid(column=2, row=3, sticky=(E,S))
print ("The current working directory is %s" % current_directory)
print ("The database working directory is %s" % database_directory)
print ("The secondary working directory is %s" % database_directory)


ttk.Button(mainframe, text="Start Capture", command=videoStream).grid(column=2, row=5, sticky=S)
# load OpenCV's Haar cascade for face detection from disk


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

folder_entry.focus()
root.bind('<Return>', database)

root.mainloop()

if (passValue==1):
	# initialize the video stream and allow the camera sensor to warmup
    print("[INFO] warming up camera...")
   # vs = VideoStream(src=0).start()
    vs = VideoStream().start()
      
    time.sleep(2.0)
    

	# start the app
    pba = FaceApp(vs, secondary_directory)
    pba.root.mainloop()
