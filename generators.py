# Generator = Function that behaves like an iterator (it can be used in a for loop)
#             Pauses a function, returns a value, then resumes
#             Uses 'yield' instead or 'return'
#             Iterate without loading everything into memory (ex. reading large files)
#             return = Pouring bucket
#             yield = Drip faucet

# ---------- EXAMPLE 1 ----------

def count_to(n):
   count = 1
   while count <= n:
       yield count  # Pause here and return the current value
       count += 1

number = int(input("Enter a number to count up to: "))

for n in count_to(number):
   print(n, end=" ")
print()

# ---------- EXAMPLE 2 ----------

def read_file(file_path):
   with open(file_path) as file:
       for line in file:
           yield line.strip()

filepath = "test.txt"

for line in read_file(filepath):
   print(line)

