import os
import sys

docName = input("Quick Note: ")
content = input("Content: ")
# editor = input("Open in: ")

if docName == "":
    docName = "Untitled"
#Will ensure that there isn't a doc called ".txt" 

w = open(docName + ".txt", "w+")

w.writelines(content)
# Open this note in notepad
w.close()

# if editor == "openw":
#     print()
# # print out various editors available based on the os

os.system("notepad " + docName + ".txt")
# opens the note in text editor of choice