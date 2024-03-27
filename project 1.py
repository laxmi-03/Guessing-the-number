import random
guess=random.randint(1,100)
name=input("Enter your name\n")
print(name)

for i in range(0,6):
    if i<5:
        num=int(input("Enter number\n"))
        if num<guess:
            print("It is too low")
        elif num>guess:
            print("It is too high")
        elif num==guess:
            print("Congrats! You win the game")
            break 
    else:
        print("oops!! correct number is:",guess)
        print("Try again later!!")

