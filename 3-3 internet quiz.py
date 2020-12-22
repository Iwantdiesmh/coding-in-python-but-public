score = 0
n = 4
questions = ['what question is this? ', 'what question is this? ', 'what question is this? ', 'what question is this? ']
answer = [1, 2, 3, 4]

for i in range(n):
    recieve = input(questions[i])
    if recieve == str(answer[i]):
        print('that is correct')
        score += 1
    else:
        print('that is incorrect')
        print('the correct answer is', answer[i])
print(score)
