import datetime

class CoinHup:
    def __init__(self, user_account):
        self.user_account = user_account
    def get_current_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def buy_coins(self, username):
        transaction_status = ""
        try:
            user_info = self.user_account.user_details[username]
            amount = int(input("Enter the amount of coins you want to buy: "))
            if amount > 0:
                cost = amount * 1.5 / 5
                if cost <= user_info["balance"]:
                    user_info["coins"] += amount
                    user_info["balance"] -= cost
                    print(f"{user_info['name']} bought {amount}Mi coins. For ${cost:.2f}")
                    transaction_status = f"Bought {amount}Mi coins. For ${cost:.2f}"
                else:
                    print(f"Insufficient balance to buy {amount}Mi coins. For ${cost}")
                    transaction_status = f"Insufficient balance to buy coins. Transaction canceled."
            else:
                print("Invalid amount of coins. Please enter a positive integer.")
                transaction_status = f"Invalid amount of coins. Transaction canceled."
            current_time = self.get_current_time()
            with open(f"{username}_transaction", "a") as file:
                file.write(f"{current_time}: {transaction_status}\n")   
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")
            transaction_status = f"Invalid input. Transaction canceled."
        except Exception as e:
            print("Error", e)
        user_info["transaction_history"].append(f"{current_time}: {transaction_status}")

    def swap_coins_to_money(self, username):
        money_obtained = 0 
        try:
            user_info = self.user_account.user_details[username]
            coins_to_swap = int(input("Enter the number of coins to swap to money: "))
            if coins_to_swap > 0 and coins_to_swap <= user_info["coins"]:
                money_obtained = coins_to_swap * 5 / 1.5
                user_info["balance"] += money_obtained
                user_info["coins"] -= coins_to_swap
                print(f"{user_info['name']} swapped {coins_to_swap}Mi coins for ${money_obtained:.2f}.")
                transaction_status = f"Swapped {coins_to_swap}Mi coins for ${money_obtained:.2f}."  
            elif coins_to_swap <= 0:
                print("Invalid number of coin. Please enter a positive integer.")
                transaction_status = f"Invalid number of coins. Transaction canceled."
            else:
                print("Insufficient coin to complete the swap")
                transaction_status =f"{coins_to_swap}Mi coin Swap canceled. Insufficient coin to complete the swap. "   
            current_time = self.get_current_time()
            with open(f"{username}_transaction", "a") as file:
                file.write(f"{current_time}: {transaction_status}\n")
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")
            transaction_status = f"Invalid input. Transaction canceled."
        except Exception as e:
            print("Error", e)
        user_info["transaction_history"].append(f"{current_time}: {transaction_status} ")