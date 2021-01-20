import random #so now that I think about it the user will most of the time win because of
                         #being able to predict what the cpu will do next. since the probability of playing
                         #the losing hand lessens after it is played once, but it's mostly even. It's hard to
                         #explain so I'll do it in class
rock = 33
paper = 34
scissors = 33
userpoints = 0
cpupoints = 0
rnd = 0

ls = ['rock','paper','scissors']

def cpuhand():
    hand = random.randint(1,100)
    if hand >= 0 and hand <= rock:
        ai = 'rock'
    if hand >= rock + 1 and hand <= rock + paper:
        ai = 'paper'
    if hand >= rock + paper + 1:
        ai = 'scissors'
    return ai

while True:
    print('round', rnd)
    user = input('''Do you want to use rock, paper, or scissors (no capitalization please)
''')

    if user not in ls:
        print('could not recognize input')
        continue

    cpu = cpuhand()
    print("You chose", user, "and cpu chose", cpu)

    if user == cpu:
        print("It is a tie!")
        
    elif user == 'rock' and cpu == 'scissors':
        print("User wins!")
        userpoints += 1
        
    elif user == 'scissors' and cpu == 'paper':
        print("User wins!")
        userpoints += 1
        
    elif user == 'paper' and cpu == 'rock':
        print("User wins!")
        userpoints += 1
        
    else:
        print("CPU wins!")
        cpupoints += 1


        #simplified the code a little so it only affects two variables rather than three so I could
        #make this code with more ease rather than worry about what may happen if both of them
        #go negative and how to balance that (it gets quite complicated)
        #--and changed it so it only changes when the user wins
        #--and removed it ^
        #time to unindent everything

        #just realize that this poses a number of problems in of itself but I'll revist this when I
        #get the other code working

        #it's been 30 minutes and I'm still trying to figure out how this works ahaha
        #edit: time to add new code up here. Finally figured it out.
        
    if user == 'rock' and scissors < 15:
        scissors += 10
        paper -= 10
    elif user == 'scissors' and paper < 15:
        paper += 10
        rock -= 10
    elif user == 'paper' and rock < 15:
        rock += 10
        scissors -= 10
                
        #basically what this code does is that, for example, play 8 rocks in a row, the scissors will be 20% or lower.
        #and since the system detects that 'hey this person isn't playing 50 rocks in a row anymore and using the
        #80% paper percentages to win a good amount of rounds by playing scissors over and over again.'
        #basically it detects the abuse of the system and soft resets it meaning that the player cant abuse the
        #high percentages

        #this may or may not work.

        #I can feel my sanity dropping already 

    if user == 'rock':
        if scissors >= 15:
            scissors -= 5
            paper += 5 
    elif user == 'scissors':
        if paper >= 15:
            rock += 5
            paper -= 5
    elif user == 'paper':
        if rock >= 15:
            rock -= 5
            scissors += 5       

    #I want to say something is wrong with my code, but I'm out of brain juice and I've complicated it so much
    #that it's hard to track down at this point.

    print('User has', userpoints, 'points. Cpu has', cpupoints)
    rnd += 1

    print(rock)
    print(paper)
    print(scissors)

    


