try:
  for i in ['a','b','c']:
    print(i**2)
except:
  print("unsupported operand types")

print()


x = 5
y = 0
try:
  z = x/y
except ZeroDivisionError:
  print("got ZeroDivisionError")
finally:
  print("All done")

print()


def ask():
  while True:
    try:
      num = int(input("Enter a number\n")) ** 2
      print(f"squared value is  {num}")
    except:
      print("Invalid Input. Try again.\n")
    else:
      print("Thank You")
      break

ask()




