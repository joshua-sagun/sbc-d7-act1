import random 
user = {}

def sign_up():
    user_id = random.randint(0, 999)
    while user_id in user:
        user_id = random.randint(0, 999)
    first_deposit = int(input("Enter Amount: "))
    if first_deposit >= 0:
        user[user_id] = first_deposit
        print(f"Account Successfully Created for: {user_id}")
    else:
        print("Enter Proper Amount")

def delete_acc(user_id):
    if user_id in user:
        del user[user_id]
        print(f"User {user_id} Has been deleted successfully!")
    else:
        print("User Id ain't found")

def withdraw(user_id, amount):
    if user_id in user:
        if 0 < amount <= user[user_id]:
            user[user_id] -= amount
            print(f"{amount} Has been withdrawn from your account")
        else:
            print("Balance is insufficient")
    else:
        print("User Id ain't found")            
        
def deposit(user_id, amount):
    if user_id in user:
        if amount > 0:
            user[user_id] += amount
            print(f"{amount} has been deposited to your account")
        else:
            print("Invalid input")
    else:
        print("User Id ain't found")

def check_balance(user_id):
    if user_id in user:
        print(f"The balance for user{user_id} is currently {user[user_id]}")
    else:
        print("User Id ain't found")

while True:
    print("""Menu:
          1. Create Account
          2. Check Balance
          3. Deposit
          4. Withdraw
          5. Delete Account
          6. Exit""")

    choice = int(input("Select one operation: "))

    if choice == 1:
        sign_up()
    elif choice == 2:
        user_id = int(input("Enter User Id: "))
        check_balance(user_id)
    elif choice == 3:
        user_id = int(input("Enter user Id: "))
        amount = int(input("Enter amount to deposit: "))
        deposit(user_id, amount)
    elif choice == 4:
        user_id = int(input("Enter User Id: "))
        amount = int(input("Enter amount to withdraw: "))
        withdraw(user_id, amount)
    elif choice == 5:
        user_id = int(input("Enter User Id to delete: "))
        delete_acc(user_id)
    elif choice == 6:
        print("Thanks!")
        break
    else:
        print("Invalid Command")
