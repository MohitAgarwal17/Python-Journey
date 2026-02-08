name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

# length = len(name)
# index = name.find("a")
# index = name.rfind("a") # gives the last occurrence of a particular element
# name = name.capitalize() # capitalizes the first letter
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha() # will give false if there is a special character
result = phone_number.count("9")
phone_number = phone_number.replace("-", "")
phone_number = phone_number.replace("-", " ")
print(result)
print(phone_number)
# print(help(str)) # will give list of all string functions
username = input("Enter a username: ")
# print(username.find(" ")) # returns -1 if no spaces are found

if len(username) > 12:
   print("Your name can't be more than 12 characters")
elif not username.find(" ") == -1: # means if result is not -1
   print("Your username can't contain spaces")
elif not username.isalpha():
   print("Your username can't contain digits")
else:
   print(f"Welcome {username}!")