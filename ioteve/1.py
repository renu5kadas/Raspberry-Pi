from random import choice
cpu = choice(('rock','paper','scissors'))
p1 = input(' rock, paper, or scissors? ')
rock = 1
paper = 2
scissors = 3
if(cpu == rock)and(p1 == rock):
    print('You Tied')
elif(cpu == rock)and(p1 == paper):
    print('You Win')
elif(cpu == rock)and(p1 == scissors):
    print('You Lose')
elif(cpu == paper)and(p1 == rock):
    print('You Lose')
elif(cpu == paper)and(p1 == paper):
    print('You Tied')
elif(cpu == paper)and(p1 == scissors):
    print('You Win')
elif(cpu == scissors)and(p1 == rock):
    print('You Win')
elif(cpu == scissors)and(p1 == paper):
    print('You Lose')
elif(cpu == scissors)and(p1 == scissors):
    print('You Tied')
