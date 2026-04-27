name = "Harshal"
city = "Nottingham"
text = """This is 
multi-line string"""


# print(text)

#indexing
print(city[4])


#slicing
print(name[0:5])
print(name[::4])
print(name[::-2])


#immutability
name = "Alex"
new_name = "J"+name[1:]
print(new_name)


#Concentration
first = "Harshal"
second = "Bolake"
print(first + " " + second)

print("Hi" * 3)


text = "python"
print(text.upper())
print(text.lower())
print(text.capitalize())

text = "hello world"
print(text.find("world"))
print("world" in text)


print(text.replace("h","j"))

print(text.strip())


splitText = "My Name is Harshal"
words = splitText.split()
print(words)


joinResult = " ".join(words)
print(joinResult)




#Example
inputName = input("Enter your name:")
print(inputName[0])
print(inputName[-1])
print(inputName[::-1])
print(inputName.upper())



