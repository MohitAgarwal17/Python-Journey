for x in range(1, 11):
    print(x, end=" ")

for x in reversed(range(1, 11)):
    print(x, end=" ")

print("Happy New Year!")

for x in range(1, 11, 2):
    print(x, end=" ")

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x, end=" ")

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x, end=" ")

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x, end=" ")

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
   for y in range(columns):
       print(symbol, end=" ")
   print()
