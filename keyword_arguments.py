# keyword arguments = arguments prefixed with the names of parameters
#                     order of the arguments doesn’t matter
#                     helps with readability

# ----- EXAMPLE 1 -----
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(greeting="Hello", title="Mr.", last="John", first="James")  # keyword arguments should be after positional arguments
# hello("mohit",greeting="Hello", title="Mr.", last="John") # this won't work as position matters
# ----- EXAMPLE 2 -----
for number in range(1, 11):
    print(number, end=" ")

print("1", "2", "3", "4", "5", sep="-")

# ----- EXERCISE -----
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=91, area=123, first=456, last=7890)
print(phone_num)