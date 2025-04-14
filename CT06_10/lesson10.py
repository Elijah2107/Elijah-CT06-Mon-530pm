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

# age = int(input("What is your age? "))
# if age < 13:
#     print("Child")


# Task 6

# Task 9

# score = int(input("What is the score? "))
# if score >= 90:
#     print("You got an A. Well done!")
# elif score >= 80 and score < 90:
#     print("You got a B. Great job!")
# elif score >= 70 and score < 80:
#     print("You got a C. Good! ")
# elif score >= 60 and score < 70:
#     print("You got a D. Not bad.")
# elif score >= 50 and score < 60:
#     print("You got a E. Pay attention to class!")
# else:
#     print("You got a F. You failed! LOL!")

# Task 10

age = int(input("What is your age? "))
if age < 0:
    print("Age cannot be negative")
elif age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")