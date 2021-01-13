import random
#there's really not much depth I can add to this. This code is mostly just someone
#asks a question and there's a random response. I don't really know what more I
#can add to that

def eightball():
    response = ['As I see it, yes.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.','Don’t count on it.','It is certain.','It is decidedly so.','Most likely.','My reply is no.','My sources say no.','Outlook not so good.','Outlook good.','Reply hazy, try again.','Signs point to yes.','Very doubtful.','Without a doubt.','Yes.','Yes – definitely.','You may rely on it.']
    input('''Please ask your yes/no question
''')
    print(response[random.randint(0,19)])


while True:
    eightball()
    fillervariable = input('''type y to continue, n to quit.
''')
    if fillervariable == 'n':
        break
