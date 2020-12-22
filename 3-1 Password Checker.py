password = str('thisisfake')
attempt = input('what is the password: ')
while attempt != password:
    print('that is incorrect')
    attempt = str(input('what is the password: '))
print('that is correct')
