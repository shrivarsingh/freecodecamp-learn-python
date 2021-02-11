
# "r" - read from file (can only read)
# "w" - write to file (can only write)
# "a" - append to file (can only add)
# "r+" - read and write

employee_file = open("employees.txt", "r")

# print(employee_file.readable()) #  check if readable

# print(employee_file.read()) # Reads document as is

# print(employee_file.readline()) # Reads first line
# print(employee_file.readline()) # Reads next line

# print(employee_file.readlines()) # Reads whole document but saves it in a list
# print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close() # Always close a file