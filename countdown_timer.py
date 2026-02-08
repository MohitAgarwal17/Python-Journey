import time

my_time = int(input("Enter the time in seconds: "))

# for x in reversed(range(0, my_time)): or (both are same)
for x in range(my_time, 0 ,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    # minutes = int(x // 60) # floor division gives the quotient, will give 61 for 3700 seconds
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")