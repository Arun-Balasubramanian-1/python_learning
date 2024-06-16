from IPython.display import clear_output
from colorama import Fore, Back, Style

GAME_ON = "game on"
GAME_OVER = "game_over"
PLAYER_1 = "X"
PLAYER_2 = "O"
count = 0
play = True
list = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',]

def display_list(list,):
  print(f"----------")
  print(f"{list[0]} | {list[1]} | {list[2]}")
  print(f"----------")
  print(f"{list[3]} | {list[4]} | {list[5]}")
  print(f"----------")
  print(f"{list[6]} | {list[7]} | {list[8]}")
  print(f"----------\n")
  print(Style.RESET_ALL)

def get_user_value(count):
  if(count%2==1):
    print(Fore.BLUE + "Player 1's choice\n")
    return 'X'
  else:
    print(Fore.MAGENTA + "Player 2's choice\n")
    return 'O'

def get_user_choice(list):
  user_choice = -1
  invalid_choice = True
  while invalid_choice:
    print(Style.RESET_ALL)
    user_choice = input("Enter a position between 1-9: ")
    if(user_choice.isdigit() and (int(user_choice) in range(1,10)) and list[int(user_choice) - 1] == ' '):
      invalid_choice = False
      break
    else:
      print(Fore.RED + "Invalid choice.\n")
      continue
  return int(user_choice)

def update_list(list, choice, user_value):
  list[choice - 1] = user_value
  return list

def check_list(list, user_value, count):
  result = True
  if((list[0] == list[1] == list[2] == user_value)):
    return user_value
  if((list[3] == list[4] == list[5] == user_value)):
    return user_value
  if((list[6] == list[7] == list[8] == user_value)):
    return user_value
  if((list[0] == list[3] == list[6] == user_value)):
    return user_value
  if((list[1] == list[4] == list[7] == user_value)):
    return user_value
  if((list[2] == list[5] == list[8] == user_value)):
    return user_value
  if((list[0] == list[4] == list[8] == user_value)):
    return user_value
  if((list[2] == list[4] == list[6] == user_value)):
    return user_value

  if(' ' in list):
    return GAME_ON
  else:
    return GAME_OVER


def check_result(result):
  if(result == PLAYER_1):
    print(Back.GREEN + "Player 1 won!")
    return False
  elif(result == PLAYER_2):
    print(Back.GREEN + "Player 2 won!")
    return False
  elif(result == GAME_ON):
    return True
  elif(result == GAME_OVER):
    print(Back.RED + "Game Over!")
    return False

while play:
  count += 1

  user_value = get_user_value(count)

  user_choice = get_user_choice(list)

  list = update_list(list, user_choice, user_value)

  clear_output()
  display_list(list)

  result = check_list(list, user_value, count)

  play = check_result(result)





