import random
from time import sleep
while True:
    print '\t\t\tWELCOME TO ROCK,PAPER,SCISSOR!!! '
    print '1)ROCK'
    print '2)PAPER'
    print '3)SCISSOR'
    a=input('ENTER YOUR CHOICE NUMBER FOR RESPECTIVE')
    if a==1:
        print'YOU HAVE OPTED FOR ROCK'
    if a==2:
        print'YOU HAVE OPTED FOR PAPER'
    if a==3:
        print'YOU HAVE OPTED FOR SCISSOR'
    print 'WAIT WHILE COMPUTER IS MAKING CHOICE!'
    sleep(1)
    b=random.randint(1,3)
    if b==1:
        print'COMPUTER HAVE OPTED FOR ROCK'
    if b==2:
        print'COMPUTER HAVE OPTED FOR PAPER'
    if b==3:
       print'COMPUTER HAVE OPTED FOR SCISSOR'
    if a==b :
       print"\t\tITS a TIE!!"
    if a==1 and b==2: 
       print'\t\t\tCOMPUTER HAS WON!BETTER LUCK NEXT TIME!'
    if a==1 and b==3:
       print'\t\t\tYOU HAVE WON!CONGRATULATIONS!'
    if a==2 and b==3:
       print't\t\tCOMPUTER HAS WON!BETTER LUCK NEXT TIME!'
    if a==2 and b==1:
       print'\t\t\tYOU HAVE WON!CONGRATULATIONS!'
    if a==3 and b==1:
       print'\t\t\tCOMPUTER HAS WON!BETTER LUCK NEXT TIME!'
    if a==3 and b==2:
       print'\t\t\tYOU HAVE WON!CONGRATULATIONS!'
    sleep(2)

   
    

