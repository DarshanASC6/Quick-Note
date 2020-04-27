# Have the user enter specific words
# Then have the script create and write to a new document

docName = input("Quick Note: ")
userInput = input("content: ")
# All of this should be done via a single input
# Ex: if user chooses name, change name of document; or else user edits content
if docName == "":
    docName = "Untitled"

w = open(docName + ".txt", "w+")

w.writelines(userInput)

if userInput == "Change Doc Name":
    userInput = input("")
    docName = userInput

w.close()