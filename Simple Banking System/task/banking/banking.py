import random
issued_cards = set()
accounts = []
logged = [0, 0]


def new_card():
    card = "400000" + str(random.randint(1000000000, 9999999999))
    if card not in issued_cards:
        issued_cards.add(card)
        return card
    else:
        return new_card()


def menu():
    global logged
    print("""1. Create an account
2. Log into account
0. Exit""")
    option = input()
    if option == "1":
        x = Account()
        print()
        print("Your card has been created")
        print(f"Your card number:\n{accounts[-1].card}")
        print(f"Your card PIN:\n{accounts[-1].pin}\n")
    elif option == "2":
        print()
        log_num = input("Enter your card number:\n")
        log_pin = input("Enter your PIN:\n")
        for i in accounts:
            if i.card == log_num:
                if i.pin == log_pin:
                    logged = [1, i]
                    print("\nYou have successfully logged in!\n")
                    return None
        print("\nWrong card number or PIN!\n")
    elif option == "0":
        print("\nBye!")
        logged = [3]
    else:
        print()


def log_menu():
    global logged

    print("""1. Balance
2. Log out
0. Exit""")
    option = input()

    if option == "1":
        print(f"\nBalance = {logged[1].balance}\n")
    elif option == "2":
        logged = [0, 0]
        print("\nYou have successfully logged out!\n")
    elif option == "0":
        print("\nBye!")
        logged = [3]
    else:
        print()


class Account:
    def __init__(self):
        self.card = new_card()
        self.pin = str(random.randint(1000, 9999))
        self.balance = 0
        accounts.append(self)


while logged[0] != 3:
    menu() if logged[0] == 0 else log_menu()
