# ques 5. Label the program written in problem 4 with comments
# Program to print the contents of a directory

import os

# Get the contents of the current directory
contents = os.listdir(".")

# Print each file and folder
for item in contents:
    print(item)
    