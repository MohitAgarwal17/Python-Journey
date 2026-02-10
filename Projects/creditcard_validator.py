# Python credit card validator program
# 1. Remove any - or
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input("Enter your credit card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1] # reversing the card_number
# print(card_number)

# for index, _ in enumerate(card_number): # does not traverse values
#     print(index)

for index, digit in enumerate(card_number):
    if index % 2 == 0:
        sum_odd_digits += int(digit)
    else:
        digit = int(digit) * 2
        if digit >= 10:
            sum_even_digits += (1 + digit % 10)
        else:
            sum_even_digits += digit

total = sum_odd_digits + sum_even_digits

if total % 10 == 0:
    print("Your credit card number is valid")
else:
    print("Your credit card number is not valid")

# This version also works

# for x in card_number[::2]:
#     sum_odd_digits += int(x)
#
# Step 3
# for x in card_number[1::2]:
#     x = int(x) * 2
#     if x >= 10:
#         sum_even_digits += (1 + (x % 10))
#     else:
#         sum_even_digits += x

# Step 4
# total = sum_odd_digits + sum_even_digits

# Step 5
# if total % 10 == 0:
#     print("VALID")
# else:
#     print("INVALID")