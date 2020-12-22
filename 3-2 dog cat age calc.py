dy1 = 12
dy2 = 24
cy1 = 15
cy2 = 24

select = input('dog or cat: ')
if select == 'dog':
    age = int(input('enter age of animal: '))
    if age == 1:
        calc = dy1
    elif age == 2:
        calc = dy2
    else:
        age -= 2
        calc = dy2 + age*4
elif select == 'cat':
    age = int(input('enter age of animal: '))
    if age == 1:
        calc = cy1
    elif age == 2:
        calc = cy2
    else:
        age -= 2
        calc = cy2 + age*4



print(calc)
