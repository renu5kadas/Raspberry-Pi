def main():

    import random
    botHand = random.randint(1,3)

        
    userHand = input("Pick rock, paper or scissors ")
    print("You pick " + userHand)
    if(botHand == 1):
        print("Computer picks scissors")
    elif(botHand == 2):
        print("Computer picks rock")
    elif(botHand == 3):
        print("Computer picks paper")
    import time
    time.sleep(2)
    if ((userHand == 'rock' or userHand == 'Rock')and botHand == 1):
        print('You win')
    elif ((userHand == 'rock' or userHand == 'Rock')and botHand == 2):
        print('You tie.')
    elif ((userHand == 'rock' or userHand == 'Rock')and botHand == 3):
        print('You lose.')
    elif ((userHand == 'paper' or userHand == 'Paper')and botHand == 1):
        print('You lose.')
    elif ((userHand == 'paper' or userHand == 'Paper')and botHand == 2):
        print('You win!')
    elif ((userHand == 'paper' or userHand == 'Paper')and botHand == 3):
        print('You tie.')
    elif ((userHand == 'scissors' or userHand == 'Scissors')and botHand == 1):
        print('You tie.')
    elif ((userHand == 'scissors' or userHand == 'Scissors')and botHand == 2):
        print('You lose.')
    elif ((userHand == 'scissors' or userHand == 'Scissors')and botHand == 3):
        print('You win!')
    else:
        print('INVALID input, try again')
        import time
        time.sleep(1)
        main()
while (1==1):
    main()
    import time
    time.sleep(1)
    input('Press enter to start again')
