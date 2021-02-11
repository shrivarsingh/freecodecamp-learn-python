# Used for error  messages

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except: # too broad exception clause
    print("Invalid Input")


try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid Input")

try:
    value = 10 / 0
except ZeroDivisionError:
    print("Divided by zero")

try:
    value = 10 / 0
except ZeroDivisionError as err:
    print(err)