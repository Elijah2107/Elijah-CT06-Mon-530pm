# Task 1

# num = int(input("Give me a number "))
# if num >= 0:
#     print((str(num) + " " + "is postive." ))
# else:
#     print((str(num) + " " + "is negative."))

# Task 2

# import random
# num = random.randint(1,10)
# guess = int(input("Give me a number between 1 to 10. "))
# if guess == num:
#     print("Congratulations!! You did it!")
# else:
#     print("Oops, better luck next time!")

# Task 3

# password = "minecraft"
# answer = input("What's the password? ")
# if answer == password:
#     print("Login Successful")
# else:
#     print("Password Incorrect")

# Task 4

# num = int(input("Give me a number "))
# remainder = num % 2
# if remainder == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# Task 5

age = input("What is your age? ")
if age < 13:
    print("Child")
else:
    if age > 13 and age < 19:
        print("Teen")
    else:
        print("Adult")