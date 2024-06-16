def lesser_of_two_evens(a,b):
  if a%2 == 0 and b%2 ==0:
    if a<b:
      return a
    else:
      return b
  else:
    if a>b:
      return a
    else:
      return b


# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(8,4))
# print(lesser_of_two_evens(2,3))
# print(lesser_of_two_evens(7,5))


def animal_crackers(text):
  words = text.split(' ')
  if words[0][0] == words[1][0]:
    return True
  else:
    return False

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

def makes_twenty(a,b):
  if a==20 or b==20 or (a+b)==20:
    return True
  else:
    return False


# print(makes_twenty(20,10))
# print(makes_twenty(10,10))
# print(makes_twenty(30,10))
# print(makes_twenty(20,20))
# print(makes_twenty(5,20))
