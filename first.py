# function 
def get_choises():
  player_choice = input("enter a choice (rock,paper, scissors)")
  computer_choice = "paper"
  choices = {"player": player_choice, "computer": computer_choice}

  return choices


choices = get_choises()

print(choices)
print("hi there")

# dictionaries
dict = {"name":"beau", "color":choices }