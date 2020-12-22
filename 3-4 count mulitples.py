interval = int(input('what number do you want to count by: '))
n = 0
print(n)
menu = input('enter return to continue or q to quit: ')
while menu != 'q':
    n += interval
    print(n)
    menu = input('enter return to continue or q to quit: ')
