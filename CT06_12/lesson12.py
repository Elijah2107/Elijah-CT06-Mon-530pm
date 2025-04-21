# Recap

# word = input("Give me a 5 letter word that contains 1 'o' and 1 'e'. ")
# contains_o = False
# contains_i = False
# for letter in word:
#     print(letter)
#     if letter == "o":
#         contains_o = True
#     elif letter == "e":
#         contains_e = True


# if not (contains_e == True and contains_o == True):
#     print("Invalid Word")
# else:
#     print("good word: " + word)

# Task 1

# visitors = 0
# while visitors < 30:
#     visitors = visitors + 1
#     print(visitors)

# Task 3

# order = ""
# answer = input("What is your order? ")
# while answer != "end":
#     order = order + answer + ", "
#     answer = input("What is your order? ")

# print("You have ordered these items, ")
# print(order)

# Task 4

# num = 10
# print(num)
# while num > 1:
#     num = num -1
#     print(num)
# else:
#     print("Happy New Year!")
    
# Task 5

# import random
# for count in range(5):
#     num1 = random.randint(1,10)
#     num2 = random.randint(1,10)
#     question = "what is " + str(num1) + " + " + str(num2) + "? " 
#     answer = input(question)
#     answer = int(answer)
#     hidden_answer = num1 + num2
#     while not answer == hidden_answer:
#         print("Wrong! Try Again")
#         answer = input(question)
#         answer = int(answer)
#     else:
#         print("You are Correct!")

# Task 6

# import random
# num = 0
# num = random.randint(1,10000)
# while num != 4:
#     num = random.randint(1,10000)
#     print(num)