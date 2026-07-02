
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except: 
    print("An exception occured")
finally:
    print("Code executed")
#else:
 #   print("Nothing went wrong")   #executes when there is no error


# x = -1
# if x < 0:
#     raise Exception("Sorry, no number below zero")

# y = (1,2,3,4,5,6)
# z = 9
# if z not in y:
#     raise Exception("Element not present")



#Custom Exception
class insufficientbalanceError(Exception):
    pass

balance = 3000
withdraw = 4000

if withdraw > balance:
    raise insufficientbalanceError("Insufficient Balance")





# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")