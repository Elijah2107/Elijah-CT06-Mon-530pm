# Recap

balance = 1000
print("Welcome to my bank!")
answer = input("Choose the one of the following, withdraw, deposit, check balance, exit ")
while not answer == exit:
    if answer == "withdraw":
        withdrawal = int(input("How much money would you like to withdraw? "))
        if balance < withdrawal:
            print("Cannot withdraw!")
        else:
            print(balance - withdrawal)
        break
    
    if answer == "deposit":
        deposit = int(input("How much would you like to deposit? "))
        print(balance + deposit)
    
    if answer == "check balance":
        print(balance)


print("Thank you for visiting our bank! ")