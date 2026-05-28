def my_function():
    print("Hello from a functon")

# my_function()

def _square_function(num):
    return (num*num)

# print(_square_function(2))
# print(_square_function(3))
# print(_square_function(4))

def get_greeting():
    return "Hello from a function"

# print(get_greeting())

def greeting_function(name="John"):
    print("Hello",name)

# greeting_function("Tom")
# greeting_function()


# Passing list as arument
def my_fruits(fruits):
    for fruit in fruits:
        print(fruit)

fruit_list = ["Apple","Banana","Cherry"]
# my_fruits(fruit_list)

#passing dictionary as agument

def my_car(car):
    print("name:",car["name"])
    print("Model:",car["model"])

car = {
    "name":"Ford",
    "model":"Mustang"
}
# my_car(car)

#function that return list
def my_cars():
    return ["BMW","Ford","Mercedes"]

cars = my_cars()
# print(cars[0])


# *args
def my_kid(*kids):
    print(kids[1])

# my_kids("John","Tom","Jerry")

def my_info(*args):
    print("Name:",args[0])
    print("Age:",args[1])
    print("Course:",args[2])

# my_info("Harshal",22,"Software Engineering")

def wishing_function(greeting,*names):
    for name in names:
        print(greeting,name)

# wishing_function("Hello","John","Tom")

def sum_of_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total

# print(sum_of_numbers(1))
# print(sum_of_numbers(1,2,3,4,5))


def find_max_number(*nums):
    if len(nums) == 0:
        return None
    max_number = nums[0]
    for num in nums:
        if num > max_number:
            max_number = num
    return max_number
    
# print(find_max_number(3,4,2,5,6,1))



# **kwargs
def my_kids(**kids):
    print(kids["name"])

# my_kids(name = "John")


def my_info(username,**info):
    print("username:",username)
    for x,y in info.items():
        print(x,y)
  
# my_info("John",age = 22, course = "Software Engineering")


#scope
x = 300     #global

def my_function():
    global x
    x = 200     #local
    # print(x)

my_function()
# print(x)


#lambda function
x = lambda x : x+10
# print(x(10))


#Recursion
def countdown(n):
    if n<=0:
        print("Done")
    else:
        print(n)
        countdown(n-1)

# countdown(5)

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))


def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(7))