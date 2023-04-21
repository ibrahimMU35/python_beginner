import random

# function 
def get_choises():
  player_choice = input("enter a choice (rock,paper, scissors)")
  options = ["rock", "paper", "scissors"]

  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices


choices = get_choises()

print(choices)
print("hi there")

# dictionaries
dict = {"name":"beau", "color":choices }
number1 = 25
number2 = 25

if number1>number2:
  print(number1)
elif number2>number1:
  print(number2)
else:
  print('there is no result')


  food = ["pizza", "carrots", "eggs"]
  dinner = random.choice(food)
  # print(dinner)