# Task 1

# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# turtle.pendown()
# turtle.forward(100)
# turtle.mainloop()
import turtle
window = turtle.Screen()
window.setup(width = 600, height = 400)
import random
turtle.goto(0,0)
turtle.color("teal")
turtle.speed(100)

for count in range(10000):
  turtle.up()
  
  randomX = random.randint(-150, 150)
  randomY = random.randint(-100, 100)
  turtle.goto(randomX, randomY)
  turtle.write(str(randomX) + "," + str(randomY))
  turtle.down()
  
window.mainloop()