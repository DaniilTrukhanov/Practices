import os
for file in os.listdir("folder/inafolder/inanotherfolder"):
    if file.endswith(".txt"):
        print (file)