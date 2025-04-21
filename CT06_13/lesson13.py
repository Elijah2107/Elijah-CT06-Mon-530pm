# Recap

balance = 1000
print("Welcome to my bank!")
answer = input("Choose the one of the following, withdraw, deposit, check balance, exit ")
while not answer == exit:
    if answer == "withdraw":
        withdrawal = input("How much money would you like to withdraw? ")
        if balance < withdrawal:
            print("Cannot withdraw!")
        else:
            print(balance - withdrawal)
    
    if answer == "deposit":
        deposit = input("How much would you like to deposit? ")
        
