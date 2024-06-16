def has_33(nums):
  length = len(nums)
  for index, item in enumerate(nums):
    if(index == (length-1)):
      break
    if(nums[index] == 3 and nums[index]==nums[index+1]):
      return True
  return False


# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))




def paper_doll(text):
  l = list(text)
  result = ''
  for item in l:
    result += 3 * item
  return result


# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))


def blackjack(a,b,c):
  sum = a + b + c
  if sum <= 21:
    return sum
  elif 11 in (a,b,c):
    sum -= 10

  if sum > 21:
    return 'BUST'
  else:
    return sum

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))

def summer_69(arr):
  if len(arr) == 0:
    return 0
  
  sum = 0
  flag = False

  for item in arr:
    if item == 9:
      flag = False
      continue
    if flag or item == 6:
      flag = True
      continue
    sum += item
  
  return sum

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))




