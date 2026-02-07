friends = ["Ashmit", "Jotisman", "Adesh"]

for letter in "Girrafe Academy":
    print(letter, end = "") # end allows to not print in next line

for friend in friends:
    print(" " + friend , end = "")

for index in range(len(friends)):
    print(" " + friends[index] , end = "")

for index in range(10): # (3,10) also works for 3 to 9
    print(index, end = " ")

for index in range(3,10): 
    print(index, end = " ")