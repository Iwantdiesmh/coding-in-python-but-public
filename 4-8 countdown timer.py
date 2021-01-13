import time
second = int(input('''Please put how many seconds you want the timer to last:
'''))

print(second)
while second != 0:
    time.sleep(1)
    second -= 1
    print(second)

print('your timer is up')
