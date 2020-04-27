# Have the user enter specific words
# Then have the script create and write to a new document

docName = input("Name of Document: ")
userInput = input("")
content = input("")
# All of this should be done via a single input
# Ex: if user chooses name, change name of document; or else user edits content

if docName == "":
    docName = "Untitled"

w = open(docName + ".txt", "r+")

if userInput == "Edit":
# What the hell is this and why the hell does it work?
    w.writelines(content)

if userInput == "Change Doc Name":
    userInput = input("")
    docName = userInput

if userInput == "Close Document":
    w.close()
# This doesn't work. This should close the document without making any changes.

# I really want to rewrite the above to be more flexible

w.close()