import random

rock = 33
paper = 34
scissors = 33
userpoints = 0
cpupoints = 0
rnd = 1

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

#there is still quite a big problem. When paper and scissors are both <15, this can cause one to shoot
#into the negative. Angus, please fix.

#update: should be fixed. I added another code though I'm suprised it didn't break because I accidentally
#typed "if rock < 15 < scissors > 40:" and that somehow worked. Now it's back to if "rock < 15 and scissors > 40:"

    if user == 'rock':
        if rock < 15 and scissors > 40:
            rock += 10
            paper += 5
            scissors -= 15
        elif scissors - 6 < 0 or rock -2 < 0:
            scissors = scissors #filler code that I'll change when I figure out a way to do it
        else:
            rock -= 2
            scissors -= 6
            paper += 8
            
    if user == 'paper':
        if paper < 15 and rock > 40:
            paper += 10
            scissors += 5
            rock -= 15
        elif rock - 6 < 0 or paper - 2 < 0:
            rock = rock
        else:
            paper -= 2
            rock -= 6
            scissors += 8
            
    if user == 'scissors':
        if scissors < 15 and paper > 40:
            scissors += 10
            rock += 5
            paper -= 15
        elif paper - 6 < 0 or scissors - 2 < 0:
            paper = paper
        else:
            scissors -= 2
            paper -= 6
            rock += 8


    print('''''')
    print('User has', userpoints, 'points. Cpu has', cpupoints, 'points')
    rnd += 1

    print('rock =', rock)
    print('paper =', paper)
    print('scissors =', scissors)
    print('')

    


