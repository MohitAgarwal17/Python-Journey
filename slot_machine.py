import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]
    # results = [] can also be done
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

def print_row(row):
    print("**************")
    print(" | ".join(row)) # joins " | " after every element in row
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100
    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current Balance: ${balance:.2f}")
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print()
            print("Please enter a valid number")
            print()
            continue

        bet = int(bet)

        if bet > balance:
            print()
            print("Insufficient funds")
            print()
            continue

        if bet <= 0:
            print()
            print("Bet must be greater than 0")
            print()
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout:.2f}")
        else:
            print(f"Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break
    print("*******************************************")
    print(f"Game over! Your final balance is ${balance:.2f}")
    print("*******************************************")

if __name__ == "__main__":
    main()