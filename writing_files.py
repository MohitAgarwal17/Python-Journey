employee_file = open("employees.txt", "a") # if i use 'w' it will over write the entire file
employee_file.write("Toby - Human Resources") # will add the text the number of times you run the code
employee_file.write("\nKelly - Customer Service")

employee_file = open("employees1.txt", "w") # will create a new file
employee_file.write("\nKelly - Customer Service")