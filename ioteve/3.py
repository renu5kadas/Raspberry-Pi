import random
rounds = 1 

def computer():
    choice = ["Rock", "Paper", "scissors"]
    random_choice = random.randrange(0, 3)
    print "Computer chose", choice[random_choice]
    
while rounds < 4: 
    print "Round", rounds
    print input("  Lets play rock, paper, scissors. Press 1 for rock, 2 for paper and 3 for scissors:")
    if input == 1:
        print "You chose rock"
    elif input == 2:
        print "You chose paper"
    elif input == 3:
        print "You chose scissors"
    elif input > 3:
        print "That's not an option"
        continue 
    
    if input == computer():
        print "It's a draw"
        rounds += 1 
    elif input == 1 and computer() == "scissors":
        print "You won"
        rounds += 1 
    elif input == 3 and computer() == "rock":
        print "You lose"
        rounds += 1 
    elif input == 1 and computer() == "paper":
        print "You lose"
        rounds += 1 
    elif input == 2 and computer() == "rock":
        print "You won"
        rounds += 1 
    elif input == 2 and computer() == "scissors":
        print "You lose"
        rounds += 1 
    else:
        print "You won"
        rounds += 1
