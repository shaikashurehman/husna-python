import random
playing=True
number=str(random.randint(0,9))
while playing:
    guess=input("tell me ur guess")
    if number==guess:
        print("you win")
        break
    else:
        print("try again")