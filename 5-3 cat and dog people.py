from tkinter import *
import random

catperson = 0
dogperson = 0

window = Tk()
window.title('pain')

canvas = Canvas(window, width=400, height = 400, bg = 'black')
canvas.pack

title = canvas.create_text(200, 200, text = 'Are you a dog or cat person?')

def cat():
    global catperson
    catperson += 1
    counter1.config(text="Cat People: " + str(catperson))

def dog():
    global dogperson
    dogperson += 1
    counter2.config(text="Dog People: " + str(dogperson))

button1 = Button(window, text = 'Cat Person', command = cat)
button1.pack()

button2 = Button(window, text = 'Dog Person', command = dog)
button2.pack()

counter1 = Label(window, text="Cat People: " + str(catperson))
counter1.pack()
counter2 = Label(window, text="Dog People: " + str(dogperson))
counter2.pack()

display_area = Label(window, text ="")
display_area.pack()

window.mainloop()
