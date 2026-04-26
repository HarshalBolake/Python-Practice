#No need to define type python is dynamically typed


name = "Harshal"
age = 21
height = 5.11
is_student = True

# Reassign Variable
age = 22

print("Name: ",name);
print("Age: ",age);


# Naming Rules
name = "Harshal"
age1 = 21
_user = "Admin"
total_marks = 90

#Not-Allowed
# 1name = "Harshal" 
# my-name = "Harshal"
# class = "Harshal"

#Official Naming Rulkes
#-start with = letters(a-z.A-Z), underscore _
#can Contain = letters, numbers, underscore



#variables are case sensitives
country = "India"
Country = "United Kingdom"

print("country: ",country);
print("Country: ",Country);


#Reserved Keywords (if, else, for, while, class, def, True, False, None)


#Naming Conversion
#Python Follows snake_case
user_name = "Harshal"
total_price = 100
is_logged_in = True


#Multiple Variables
a, b, c = 1, 2, 3
x = y = z = 0;

print(a);
print(b);
print(c);
print(x);
print(y);
print(z);



#Example 1
product_name = "Laptop"
price = 50000
discount = 2000

final_price = price - discount

print("Product: ",product_name)
print("Final Price: ",final_price)


#Example 2
name = "Harshal"
age = 22
love = "python"

print("My name is", name ,"I am", age ,"years old, and I love", love , ".");



#Variables sotores (addresses) to objects in memory not values
x = 10
y = x
print(id(x))
print(id(y))

y = 20
print(id(y));


#mutable & immutable
#Variables are immutable (Cannot change)

#mutable objects -> list, dict, set
numbers = [1, 2, 3]
numbers[0] = 100
#numbers = [100, 2, 3]



#Data types
# int = 10
# float = 10.5
# str = "Hello"
# bool = True, False
# list = [1,2,3]
# tuple = (1,2,3)
# dict = {"a":1, "b":2}
# set = {1,2,3}