#def add():
#    return 1 + 1

#    print(1 - 1)

#num = add()
#num2 = sub()

#print(num)
#print(num2)

#def add(x):
#    print(x + 1)

#i = 142
#add(i)

#def triangle(b1, b2, g1):
#    print(f"{b1} likes {g1}")
#    print(f"{b2} likes {g1}")

#triangle( b1="jj", g1="bb", b2="n")

#def names(*args):
#    for arg in args:
#        print(arg)

#names("l", "b", "c",000000 "j")

#from random import randint
#id = []

#def create_user(): vbr

accounts = {}

def create_account(account_holder_name):
    if account_holder_name not in accounts:
        accounts[account_holder_name] = 0
        print(f"Account for {account_holder_name} created successfully.")
    else:
        print(f"Account for {account_holder_name} already exists.")

def check_balance(account_holder_name):
    if account_holder_name in accounts:
        balance = accounts[account_holder_name]
        print(f"{account_holder_name}'s balance: ₱{balance}")
    else:
        print(f"Account for {account_holder_name} does not exist.")

def deposit(account_holder_name, amount):
    if account_holder_name in accounts:
        accounts[account_holder_name] += amount
        print(f"Deposited ₱{amount} into {account_holder_name}'s account.")
    else:
        print(f"Account for {account_holder_name} does not exist.")

def withdraw(account_holder_name, amount):
    if account_holder_name in accounts:
        if accounts[account_holder_name] >= amount:
            accounts[account_holder_name] -= amount
            print(f"Withdrew ₱{amount} from {account_holder_name}'s account.")
        else:
            print(f"Insufficient funds for {account_holder_name}.")
    else:
        print(f"Account for {account_holder_name} does not exist.")

def delete_account(account_holder_name):
    if account_holder_name in accounts:
        del accounts[account_holder_name]
        print(f"Account for {account_holder_name} deleted successfully.")
    else:
        print(f"Account for {account_holder_name} does not exist.")

# Example usage:
while True:
    print("\nOptions:")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Account")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter account holder name: ")
        create_account(name)
    elif choice == 2:
        name = input("Enter account holder name: ")
        check_balance(name)
    elif choice == 3:
        name = input("Enter account holder name: ")
        amount = float(input("Enter deposit amount: "))
        deposit(name, amount)
    elif choice == 4:
        name = input("Enter account holder name: ")
        amount = float(input("Enter withdrawal amount: "))
        withdraw(name, amount)
    elif choice == 5:
        name = input("Enter account holder name: ")
        delete_account(name)
    elif choice == 6:
        print("Exiting bank system. Have a great day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")