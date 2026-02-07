# open("employees.txt", "r+") # r+ for read and write
# open("employees.txt", "w") # w for write
# open("employees.txt", "a") # a for append at the end, cant modify the information of the file

employee_file = open("employees.txt", "r") # r for read
print(employee_file.readlines()[1])
print(employee_file.readlines())
print(employee_file.readable()) # shows if a file is readable or not
print(employee_file.read())
print(employee_file.readline()) # will work without read as read prints the whole file
print(employee_file.readline())
print(employee_file.readlines())
# a = open("employees.txt", "r") # r for read
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
