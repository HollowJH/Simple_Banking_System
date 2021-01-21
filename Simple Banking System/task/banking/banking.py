from random import randint
issued_cards = set()
accounts = []
logged = [0, 0]


def new_card():
    card = "400000" + f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}" \
                      f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
    if card not in issued_cards and luhn(card):
        issued_cards.add(card)
        return card
    else:
        return new_card()


def luhn(card):
    last_digit = card[-1]
    card = card[:-1]
    card = [str(int(card[i]) * 2) if (i+1) % 2 == 1 else card[i] for i in range(len(card))]
    card = [str(int(card[i]) - 9) if int(card[i]) > 9 else card[i] for i in range(len(card))] + [last_digit]
    m10 = sum(list(map(int, card)))
    return m10 % 10 == 0


def menu():
    global logged
    print("""1. Create an account
2. Log into account
0. Exit""")
    option = input()
    if option == "1":
        _ = Account()
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
        self.pin = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
        self.balance = 0
        accounts.append(self)


while logged[0] != 3:
    menu() if logged[0] == 0 else log_menu()
