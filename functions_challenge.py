def spy_game(nums):
  result = ''
  for item in nums:
    if item in (0,7):
      result += str(item)
  return '007' in result


# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

import math

def count_primes(num):
  count = 0
  for item in range(2,num+1):
    flag = True
    for num in range(2, math.floor(item/2) + 1):
      if(item%num == 0):
        flag = False
        continue 
    if flag:
      count += 1
  
  return count

# print(count_primes(10))
# print(count_primes(100))
