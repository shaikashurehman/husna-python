class dog:
    animal="dog"
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour
dog1=dog("Labrador","brown")
dog2=dog("pug","white")
print(dog.animal,dog1.breed,dog1.colour)
print(dog.animal,dog2.breed,dog2.colour)