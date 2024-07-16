#Copy the file and move it to a new location
import os
import shutil
src = "/home/mubashar/Desktop/Lab 12/Today's Lab.txt"
des = "/home/mubashar/Desktop/folder/Today's Lab.txt"
change_location = shutil.copyfile(src, des)
