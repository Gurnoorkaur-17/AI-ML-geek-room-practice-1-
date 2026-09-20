# ques 4. write a python program to print the contents of a directory using the os module. search online for the function which does that.

import os

contents = os.listdir(".")

for item in contents:
    print(item)