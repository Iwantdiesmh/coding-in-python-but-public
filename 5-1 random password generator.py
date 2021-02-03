from tkinter import *
import random
Uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Lowercase = ['a','b','c','d','e','f','g','h','i','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Symbols = ['!','@','#','$','%','&']
Numbers = ['1','2','3','4','5','6','7','8','9','0']
password = ''
length = random.randint(4,10)

def randompassword(length):
    global password
    while length != 0:
        number = random.randint(1,4)
        if number == 1:
            password = password + random.choice(Uppercase)
        if number == 2:
            password = password + random.choice(Lowercase)
        if number == 3:
            password = password + random.choice(Symbols)
        if number == 4:
            password = password + random.choice(Numbers)
        length -= 1

randompassword(length)

window = Tk()
window.title('Password Generator')

def password_generator():
   print(password)
   display_area.config(text = password, fg = 'black', bg = 'white')

button1 = Button(window, text = 'Generate Password', command = password_generator)
button1.pack()

display_area = Label(window, text ="")
display_area.pack()

window.mainloop()
