import random

# function 
def get_choises():
  player_choice = input("enter a choice (rock,paper, scissors)")
  options = ["rock", "paper", "scissors"]

  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices

# function arguments
def check_win(player, computer):
  # print("you chose " + player + " ,computer chose " + computer)

  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "it's a tie"
  elif player == "rock":
      if computer == "scissors":
         return "Rock smashes scissors! You win"
      else:
         return "Paper covers rock! You lose"
  elif player == "paper":
      if computer == "scissors":
         return "Paper covers rock! You win"
      else:
         return "Scissors cuts paper! You lose"
  elif player == "scissors":
      if computer == "paper":
         return "Scissors cuts paper! You win"
      else:
         return "Rock smashers scissors! You lose"
      
choices = get_choises()
      
  # elif player == "rock" and computer == "scissors":
  #   return "Rock smashes scissors! You win!"
  # elif player == "rock" and computer == "paper":
  #   return "Paper covers rock! You lose!"
# check_win("rock", "paper")
# we can use fstring

# age = 25 
# print(f"jim is {age} years old")




# a = 3
# b = 5
# if a == b:
#   print(yes)


# choices = get_choises()

# print(choices)
# print("hi there")

# # dictionaries
# dict = {"name":"beau", "color":choices }
# number1 = 25
# number2 = 25

# if number1>number2:
#   print(number1)
# elif number2>number1:
#   print(number2)
# else:
#   print('there is no result')


#   food = ["pizza", "carrots", "eggs"]
#   dinner = random.choice(food)
#   # print(dinner)