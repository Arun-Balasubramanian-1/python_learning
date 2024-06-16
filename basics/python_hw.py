

def vol(rad):
    return (4/3)*(3.14)*(rad**3)


#print(vol(2))

def ran_check(num,low,high):
    result = num in range(low, high+1)
    if result:
      print(f'{num} in range')
    else:
      print(f'{num} not in range')


# ran_check(5,2,7)
# ran_check(2,2,7)
# ran_check(7,2,7)
# ran_check(1,2,7)
# ran_check(8,2,7)



def up_low(s):
    upper = 0
    lower = 0
    for item in s:
      if item.isupper():
        upper += 1
      elif item.islower():
        lower += 1
    
    print(f'Original String : {s}')
    print(f'No. of Upper case characters : {upper}')
    print(f'No. of Lower case Characters : {lower}')


# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)


def unique_list(lst):
    return list(set(lst))

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


def multiply(numbers):  
    result = 1
    for item in numbers:
      result *= item
    
    return result

#print(multiply([1,2,3,-4]))




def palindrome(s):
    return s == s[::-1]

# print(palindrome('helleh'))
# print(palindrome('hello'))



import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    
    for item in str1:
      alphabet = alphabet.replace(item.lower(), "")

    return alphabet == ""


# print(ispangram("The quick brown fox jumps over the lazy dog"))