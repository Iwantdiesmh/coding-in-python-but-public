import random
ls = ['polish','adjoining','credit','airplane']
score = 0

def scramble(w):
    letters = list(w)
    random.shuffle(letters)
    scramble_word = ''
    for i in letters:
        scramble_word = scramble_word + i
    return scramble_word

random.shuffle(ls)
for word in ls:
    new_word = scramble(word)
    print('your scrambled word is:', new_word)
    response = input('please type the original word: ')
    if response == word:
        print('you are correct')
        score += 1 
        
    else:
        print('the correct word is:', word) #make a hint system

    asktoquit = input('do you want to quit [y/n] ')
    if asktoquit == 'y' or 'yes':
        break      

print('you have done all the words')
print('you have gotten', score, 'correct')
 
print('--j--n---')
