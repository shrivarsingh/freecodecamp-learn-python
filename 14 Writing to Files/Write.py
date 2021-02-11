
# append
# employee_file = open("employees.txt", "a")
# employee_file.write("\nKelly - Customer Services")
# employee_file.close()

employee_file = open("employees1.txt", "w") # can create a new file and overwrite all data in the old one
employee_file.write("\nKelly - Customer Services")
employee_file.close()

web_file = open("index.html", "w")
web_file.write("<p>This is HTML</p>")
web_file.close()