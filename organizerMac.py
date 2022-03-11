import os
import shutil

keyWords = []
while True:
    keyWord = input("What word would you like to sort by? ")
    keyWords.append(keyWord)

    cont = input("Would you like to input more words? (y for yes, anything else for no) ")

    if cont != "y":
        break

print(keyWords)

path = input("path: ")
files = os.listdir(path)

for word in keyWords:
    isExist = os.path.exists(path + "/" + word)

    if not isExist:
        os.makedirs(path + "/" + word)

for file in files:
    file = os.path.relpath(file)
    
    for word in keyWords:
        if word.lower() in file.lower():
            if file != word:
                shutil.move(path + '/' + file, path + '/' + word + '/' + file)