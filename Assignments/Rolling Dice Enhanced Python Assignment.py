import random

print('Welcome to playing my rolling dice game!')


num_guesses = int(input('Please enter the number of chances you would like: '))

                  

dice = []
dice.append(random.randint(1,6))


dice.append(random.randint(1,6))


total = sum(dice)


for i in range(num_guesses):
    guess = int(input('What is your guess for the total of the two dice: '))
    if guess == total:
        print('You win!')
        break
    elif guess > total:
        print("Your guess is too high...try again!")
    else:
        print("Your guess is too low...try again")

Quit = input("Would you like to keep playing? (Y/N): ")

while (Quit.lower()== "y"):
    if (Quit.lower()== "y"):
        num_guesses = int(input('Please enter the number of chances you would like: '))

        dice = []
        dice.append(random.randint(1,6))
        dice.append(random.randint(1,6))
        total = sum(dice)


        for i in range(num_guesses):
            guess = int(input('What is your guess for the total of the two dice: '))
            if guess == total:
                print('You win!')
                break
            elif guess > total:
                print("Your guess is too high...try again!")
            else :
                print("Your guess is too low...try again")

    Quit = input("Would you like to keep playing? (Y/N): ")
        

    if (Quit.lower()=="n"):
        print("Goodbye")
        break
    
    while (Quit.lower()!= "y" or Quit.lower() != "n"):
            print("Sorry, input not recognized.")
            Quit = input("Would you like to keep playing? (Y/N): ")
        
