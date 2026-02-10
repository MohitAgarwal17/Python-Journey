# ---------- script1.py ----------
# This file can run standalone or be imported

print(__name__)
def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__': # when we run script2 this will not run as at that time __name__ != __main__
    main()