import random #so now that I think about it the user will most of the time win because of
                         #being able to predict what the cpu will do next. since the probability of playing
                         #the losing hand lessens after it is played once, but it's mostly even. It's hard to
                         #explain so I'll do it in class
rock = 33
paper = 34
scissors = 33
userpoints = 0
cpupoints = 0

while True:
    def cpuhand():
        hand = random.randint(1,100)
        if hand >= 0 and hand <= rock:
            ai = 'rock'
        if hand >= rock + 1 and hand <= rock + paper:
            ai = 'paper'
        if hand >= rock + paper + 1:
            ai = 'scissors'
        return ai

    user = input('''Do you want to use rock, paper, or scissors (no capitalization please)
''')

    #while user != 'rock' or user != 'scissors' or user != 'paper':
        #print('please type "rock", "paper", or "scissors". Case sensitive.')
        #user = input('''Do you want to use rock, paper, or scissors (no capitalization please)
#''')
    
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

    if user == 'rock':
        rock -= 3
        scissors -= 3
        paper += 6
    elif user == 'scissors':
        rock += 6
        scissors -= 3
        paper -= 3
    elif user == 'paper':
        rock -= 3
        scissors += 6
        paper -= 3

    print('User has', userpoints, 'points. Cpu has', cpupoints)

    print(rock)
    print(paper)
    print(scissors)

    


