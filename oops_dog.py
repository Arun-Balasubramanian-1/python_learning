class Dog():
  def __init__(self, breed):
    self.breed = breed


my_dog = Dog('Husky')

print(my_dog.breed)
print(type(my_dog))

new_dog = Dog(breed='Corgies')

print(new_dog.breed)
print(type(new_dog))