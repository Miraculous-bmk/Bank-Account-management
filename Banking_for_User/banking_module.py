from Banking_for_User.new_banking import UserAccount
import datetime

class BankingSystem:
    def __init__(self):
        self.user_account = UserAccount()
    def get_current_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
    def welcome_bonus(self, username):
        user_info = self.user_account.user_details[username]
        welcome_bonus_amount = 500
        user_info["coins"] += welcome_bonus_amount
        print(f"Welcome, {user_info['username']}! You have received {welcome_bonus_amount}Mi coins as a welcome bonus.")
        user_info["transaction_history"].append(f"{current_time}: Received a welcome bonus of {welcome_bonus_amount} Mgn coins.")
        current_time = self.get_current_time()
        with open(f"{username}_transaction", "a") as file:
            file.write("User Transaction \n")
            file.write(f"{current_time}: Received a Welcome Bonus: {welcome_bonus_amount}Mi coins\n")
            file.write(f"Remaining Balance: ${user_info['balance']:.2f}\n")
            file.write(f"Remaining coins: {user_info['coins']}Mi\n")

    def deposit_money(self, username):
        try:
            amount = float(input("Enter the amount to deposit: $"))
            if amount > 0:
                user_info = self.user_account.user_details[username]
                user_info["balance"] += amount
                print(f"Successfully deposited ${amount}. Your new balance is ${user_info['balance']:.2f}")
                transaction_status = f"Deposited: ${amount:.2f} to balance. Your new balance: ${user_info['balance']:.2f}"
            else:
                print("Invalid deposit amount. Please enter a positive amount.")
                transaction_status = "Invalid deposit amount. Transaction Cancelled."
            current_time = self.get_current_time()
            with open(f"{username}_transaction", "a") as file:
                file.write(f"{current_time}: {transaction_status}\n")           
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")
            transaction_status = f"Invalid input. Transaction Cancelled."
        except Exception as e:
            print("Error:", e)
        user_info["transaction_history"].append(f"{current_time}: {transaction_status}")

    def transfer(self, username):
        try:
            user_info = self.user_account.user_details[username]
            transfer = float(input("Enter the amount you want to transfer from your balance: $"))
            receiv_by = int(input("Enter the recipient's wallet code: "))
            if transfer > 0 and transfer <= user_info["balance"]:
                user_info["balance"] -= transfer
                print(f"Successfully transferred ${transfer}. Your new balance is ${user_info['balance']:.2f}")
                print(f"You transferred ${transfer} to wallet {receiv_by}.")
                transaction_status = f"Successfully transferred ${transfer} to this wallet {receiv_by}. New balance is ${user_info['balance']:.2f}."
            elif transfer <= 0:
                print("Invalid amount. Please enter a positive amount.")
                transaction_status = "Invalid amount. Transaction Cancelled."
            else:
                print("Insufficient balance.")
                transaction_status = f"${transfer} Transfer Cancelled. Insufficient balance: ${user_info['balance']:.2f}" 
            current_time = self.get_current_time()
            with open(f"{username}_transaction", "a") as file:
                file.write(f"{current_time}: {transaction_status}\n")
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")
            transaction_status = "Invalid input. Transaction Cancelled."
        except Exception as e:
            print("Error", e)
        user_info["transaction_history"].append(f"{current_time}: {transaction_status}")
    
    def withdraw_money(self, username):
        try:
            user_info = self.user_account.user_details[username]
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > 0 and amount <= user_info["balance"]:
                user_info["balance"] -= amount
                print(f"Successfully withdrew ${amount}. Your new balance is ${user_info['balance']:.2f}")
                transaction_status = (f"Successfully Withdrew: ${amount:.2f} from balance. Your new balance: ${user_info['balance']:.2f} ")
            elif amount <= 0:
                print("Invalid withdrawal amount. Please enter a positive amount.")
                transaction_status = "Invalid amount. Transaction Cancelled."
            else:
                print("Insufficient balance.")
                transaction_status = (f"${amount} Withdraw Cancelled. Insufficient balance: ${user_info['balance']:.2f}" )               
            current_time = self.get_current_time()
            with open(f"{username}_transaction", "a") as file:
                file.write(f"{current_time}: {transaction_status}\n")
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")
            transaction_status = "Invalid input. Transaction Cancelled."
        except Exception as e:
            print("Error:", e)
        user_info["transaction_history"].append(f"{current_time}: {transaction_status}")  

    def display_balance(self, username):
        try:
            user_info = self.user_account.user_details[username]
            print(f"{user_info['name']}'s balance: ${user_info['balance']:.2f}")
            print(f"{user_info['name']}'s coins: {user_info['coins']}Mi")
            transaction_status = f"{user_info['name']}'s Balance: ${user_info['balance']:.2f} and {user_info['coins']}Mi coins"
            current_time = self.get_current_time()
            with open(f"{username}_transaction", "a") as file:
                file.write(f"{current_time}: {user_info['name']}'s Balance: ${user_info['balance']:.2f} \n")
                file.write(f"{current_time}: {user_info['name']}'s Coins: {user_info['coins']}Mi \n")
            with open("Account Balance", "w") as file:
                file.write(f"{user_info['name']}'s Remaining Balance \n")
                file.write(f"{current_time}: Balance: ${user_info['balance']:.2f} \n")
                file.write(f"{current_time}: Coins: {user_info['coins']}Mi \n")
            user_info["transaction_history"].append(f"{current_time}: {transaction_status}")
        except FileNotFoundError:
            print("File don't exists: ")
        except Exception as e:
            print("Enter", e) 

    def transaction_history(self, username):
        user_info = self.user_account.user_details[username]
        print("Transaction History:")
        for transaction in user_info.get("transaction_history", []):
            print(transaction)
        print(f"Remaining Balance: ${user_info['balance']:.2f}")
        print(f"Remaining coins: {user_info['coins']:.2f}Mi")
        try:
            with open("transaction_history", "w") as file:
                file.write("Transaction History:\n")
                for transaction in user_info.get("transaction_history", []):
                    file.write(transaction + "\n")
                file.write(f"Remaining Balance: ${user_info['balance']:.2f}\n")
                file.write(f"Remaining coins: {user_info['coins']}Mi\n")
            print("Transaction history including remaining balance and coins has been saved to 'transaction_history.txt'.")
        except Exception as e:
            print(f"An error occurred while saving the transaction history: {str(e)}")