def old_macdonald(name):
  return name[0:3].capitalize() + name[3:].capitalize()


# print(old_macdonald('macdonald'))
# print(old_macdonald('arunbarun'))

def master_yoda(words):
  return "  ".join(words.split(' ')[::-1])


# print(master_yoda('We are ready'))
# print(master_yoda('I am Arun'))

def almost_there(n):
    if (n>=90 and n<=110) or (n>=190 and n<=210):
      return True
    else:
      return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))