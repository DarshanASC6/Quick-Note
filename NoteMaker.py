# Have the user enter specific words
# Then have the script create and write to a new document
import os

docName = input("Quick Note: ")
content = input("content: ")
# All of this should be done via a single input
# Ex: if user chooses name, change name of document; or else user edits content
if docName == "":
    docName = "Untitled"

w = open(docName + ".txt", "w+")


w.writelines(content)
# Open this note in 

w.close()