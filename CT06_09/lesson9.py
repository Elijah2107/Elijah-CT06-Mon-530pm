# Task 2

# days = 26
# if days > 25:
#     print("Remember to return your book! ")

# Task 3

# import random
# randnum = random.randint(1,10)
# guess = int(input("Give me a number between 1 to 10 "))
# print(randnum == guess)

# Task 4

# num_of_apples = int(input("How many apples do you want? "))
# cost_apple = num_of_apples * 1
# if num_of_apples > 5:
#     cost_apple = cost_apple * 0.9
# print(cost_apple)

# Task 5

# num_of_apples = int(input("How many apples do you want? "))
# num_of_oranges = int(input("How many oranges do you want? "))
# cost_apple = num_of_apples * 0.6
# cost_orange = num_of_oranges * 0.9
# if num_of_apples > 5:
#     cost_apple = cost_apple * 0.9
# if num_of_oranges > 5:
#     cost_orange = cost_orange * 0.9
# total = cost_apple + cost_orange
# print(total)

# Task 7

positive_days = 0
for count in range(1,8):
    print(count)
    temperature = int(input("What is the temperature? "))
    if temperature > 30:
        positive_days = positive_days + 1


print(positive_days)