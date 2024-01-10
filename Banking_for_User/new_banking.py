import random
import os
class UserAccount:
    def __init__(self):
        self.user_details = {}
        self.username = ""
    def sign_up(self,username, password, name:str, age:int):
        
        self.user_details[username] = {
            "password": f"Password: {password}", 
            "name": name,
            "balance": 0,
            "coins": 500,
            "transaction_history": [],
        }
        self.user_file = username + "Access.txt"
        with open(self.user_file, "w") as file:
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
        return True  
    def log_in(self, username:str, password_input):
        try:
            self.user_file = username + "Access.txt"
            if not os.path.isfile(self.user_file):
                print(f"User file not found for user {username}. Please check your username.")
                return None
            with open(self.user_file, 'r') as file:
                lines = file.readlines()
                stored_password = None
                for line in lines:
                    if line.startswith("Password: "):
                        stored_password = line[len("Password: "):].strip()
                        break
            user_data = self.user_details.get(username)
            if user_data and user_data["password"] == f"Password: {password_input}":
                return username
            else:
                print("Invalid username or password. Please try again.")
                return None
        except FileNotFoundError:
            print("User not found. Please check your username and password.")
            return None
        except Exception as e:
            print("Error:", e)
    def forgot_password(self,username):
        try:  
            user_data = self.user_details.get(username)
            if user_data is not None:
                self.user_file = username + "Access.txt"
                if os.path.exists(self.user_file):
                    reset_code = str(random.randint(1000, 9999))
                    print(f"A reset code has been sent to your registered email/phone.")
                    print(f"The code to resit your password: {reset_code}")
                    new_password = input("Enter the reset code: ")
                    if new_password == reset_code:
                        new_password = input("Enter your new password: ")
                        user_data["password"] = f"Password: {new_password}"
                        with open(self.user_file, "r+") as file:
                            lines = file.readlines()
                            lines[1] = f"Password: {new_password}\n"
                            file.seek(0)
                            file.writelines(lines)
                        print("Password reset successfully.")
                        return True
                    else:
                        print("Invalid reset code. Password reset failed.")
                else:
                    print(f"User file not found for user {username}. Please check your username.")
            else:
                print("Username not found.")
        except Exception as e:
            print("Error:", e)
