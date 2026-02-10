principle = 0
time = 0
rate = 0
# this doesn't accept zero as input
# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle can't be less than equal to zero")
#
# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can't be less than equal to zero")
#
# while time <= 0:
#     time = int(input("Enter the interest rate: "))
#     if time <= 0:
#         print("Time can't be less than equal to zero")
#
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s: ${total:,.2f}")

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the interest rate: "))
    if time <= 0:
        print("Time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:,.2f}")
