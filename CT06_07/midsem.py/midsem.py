# This program asks for a name and prints out "nice to meet you" and the name
# name = input("What is your name? ")
# print("Nice to meet you," + " " + name)
# The program asks you for three number, the start the end and the increment. When you type the answer in, the program will print the answers in order from the start to the end.
start = int(input("Which number should I start with? "))
end = int(input("Which number should I end with? "))
increment = int(input("What is the increment number? "))
for count in range(start,end,increment):
    print(count)