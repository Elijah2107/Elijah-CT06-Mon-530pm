# Recap 1
# product = 1
# for count in range(5):
#     num = input("give me a number ")
#     num = int(num)
#     product = product * num

# print("the final result is " + str(product))

# Task 1

import time
start = int(input("What is starting number? "))
stop = int(input("What is ending number? "))
step = int(input("What is the decrement? "))
for count in range(start,stop,step):
    print(count)
    time.sleep(1)

