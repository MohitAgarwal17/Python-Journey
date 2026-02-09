# *args    = allows you to pass multiple non-key arguments, passed as tuples
# **kwargs = allows you to pass multiple keyword-arguments, passed as dictionaries
#            * unpacking operator

def add(*nums):
   total = 0
   for num in nums:
       total += num
   return total

print(add(1, 2, 3, 4))

# ----- *ARGS Example 2 -----

def display_name(*args):
    # print(type(args))
   print(f"Hello", end=" ")
   for arg in args:
       print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

print()
# ----- **KWARGS -----
def print_address(**kwargs):
    # print(type(kwargs))
    for value in kwargs.values():
        print(value, end=" ")
    # for key in kwargs.keys(): # will print keyword names
    #     print(key, end=" ")

    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")

print_address(street="123 Fake St.",
              pobox="P.O Box 777",
              city="Detroit",
              state="MI",
              zip="54321")
print()
# ----- EXERCISE -----
def shipping_label(*args, **kwargs): # it will always be args first followed by kwargs
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox"and "street" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")