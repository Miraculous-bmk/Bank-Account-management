from Banking_for_User.banking_module import BankingSystem
from Banking_for_User.new_banking import UserAccount
from Banking_for_User.coin_system import CoinHup

user_banking = BankingSystem()
user_account = UserAccount()
val_error_txt = "Invalid input. Please enter valid data."
while True:
    while True:

        print("\nOptions:")
        print("1. Sign up")
        print("2. Log In")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            while True:
                print("Create an account with us:")
                try:
                    username = input("Enter a username: ")
                    password = input("Create a password: ")
                    name = input("Enter your name: ")
                    age = int(input("Enter your age:"))
                except ValueError:
                    print(val_error_txt)
                else:
                    sign_up = user_account.sign_up(username,password,name,age)
                    if sign_up == True:
                        print("Account created successfully.")
                        break
        elif choice == '2':
            while True:
                print("Log into your account:")
                try:
                    username = input("Enter your username: ")
                    password_input = input("Enter your password: ").strip()
                except ValueError:
                    print(val_error_txt)
                else:
                    logged_in_user = user_banking.user_account.log_in(username,password_input)
                if logged_in_user:
                    print("Login successful.")
                    break   
                print("Login Failed")
            break
        elif choice == "3":
            while True:
                print("Forgot Password?")
                username = input("Enter your username: ")
                reset= user_banking.user_account.forgot_password(username)
                if reset is True:
                    break
        elif choice == "4":
            exit()

    while True:
        print(f"Logged in as {logged_in_user}")
        print("Welcome, you have been given 500 miros g-network coin as a registration bonus.")
        coin_Management = CoinHup(user_banking.user_account)
        while True:
            print("\nBanking Options:")
            print("1. Deposit Money")
            print("2. Transfer Money")
            print("3. Withdraw Money")
            print("4. Buy Coin")
            print("5. Swap Coin To Money ")
            print("6. Display Balance")
            print("7. Transaction History")
            print("8. Log Out")
            banking_choice = input("Enter your banking choice (1/2/3/4/5/6/7/8): ")
            if banking_choice == '1':
                user_banking.deposit_money(username)
            elif banking_choice == '2':
                user_banking.transfer(username)
            elif banking_choice == '3':
                user_banking.withdraw_money(username)
            elif banking_choice == '4':                    
                coin_Management.buy_coins(username)
            elif banking_choice == '5':
                coin_Management.swap_coins_to_money(username)
            elif banking_choice == '6':
                user_banking.display_balance(username)
            elif banking_choice == '7':
                user_banking.transaction_history(username)
            elif banking_choice == '8':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        break