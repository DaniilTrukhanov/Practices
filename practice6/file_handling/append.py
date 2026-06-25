with open ("file.txt", "a") as file:
    file.write("\nnew line")

with open ("file.txt") as file:
    print (file.read())