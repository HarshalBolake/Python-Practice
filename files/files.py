
f = open("files/data.txt","rt")
# f.write("My Name is Harshal")
# print(f.read())

# f.close()

#alternative 
with open("files/data.txt") as f:
    # print(f.read(19))
    # print(f.readline())
    # print(f.readline())
    for x in f:
        print(x)


with open("files/data.txt", "a") as f:
    f.write("Some more content")

with open("files/data.txt", "w") as f:
    f.write("Data deleted")

with open("files/data.txt") as f:
    for x in f:
        print(x)


#Delete a file
import os
os.remove("files/data.txt")  #Delete file
os.rmdir("files")            #Delete folder