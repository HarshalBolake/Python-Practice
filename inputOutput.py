#Basics
name = input("Enter your name: ") #input() always return string
# print(name)

age = int(input("Enter your age: "))
# print(age , type(age))

#Better output formatting (f-strings)
print(f"My name is {name} and I am {age} years old")


#Special print features
#separator
print("A", "B", "C", sep="-")

#end
print("Hello", end= " ")
print("World")

#Example
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition: ", x+y)
print("Subtraction: ", x-y)
print("Multiplication: ", x*y)
print("Division: ", x/y)