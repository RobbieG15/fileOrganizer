import os
import shutil

while True:
    try:
        path = input('What path would you like to organize?\n')
        files = os.listdir(path)
        print('Valid path. Sorting...\n')
        break
    except FileNotFoundError:
        print('Path was invalid. Please try another path.')
        continue

for file in files:
    filename, fileExtention = os.path.splitext(file)
    try:
        os.makedirs(path + '/' + fileExtention[1:], exist_ok=False)
        shutil.move(path + '/' + file, path + '/' + fileExtention[1:] + '/' + file)
    except OSError:
        shutil.move(path + '/' + file, path + '/' + fileExtention[1:] + '/' + file)