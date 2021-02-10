import random
from tkinter import *

def print_song(one, two, three, four, five, six):
    print('''I am not throwing away my %s
    I am not %s away my %s
    Hey yo, I'm just like my country
    I'm %s, %s and %s
    And I'm not %s away my %s
    ''' %(one, two, three, four, five, six, two, three))

window = Tk()
window.title('Random Song')

frame5 = Frame(window)
frame5.grid(row=0,column=0,sticky='NSEW')

one = StringVar()
string_entry_value = Entry(frame5,textvariable=one,width=30)
string_entry_value.grid(row=1,column=0,sticky=W)

two = StringVar()
string_entry_value = Entry(frame5,textvariable=two,width=30)
string_entry_value.grid(row=3,column=0,sticky=W)

three = StringVar()
string_entry_value = Entry(frame5,textvariable=three,width=30)
string_entry_value.grid(row=5,column=0,sticky=W)

four = StringVar()
string_entry_value = Entry(frame5,textvariable=four,width=30)
string_entry_value.grid(row=7,column=0,sticky=W)

five = StringVar()
string_entry_value = Entry(frame5,textvariable=five,width=30)
string_entry_value.grid(row=9,column=0,sticky=W)

six = StringVar()
string_entry_value = Entry(frame5,textvariable=six,width=30)
string_entry_value.grid(row=11,column=0,sticky=W)

Label(frame5,text='A word that rhymes with "shot"').grid(row=0,column=0,sticky=W)
Label(frame5,text='A word that rhymes with "throwing"').grid(row=2,column=0,sticky=W)
Label(frame5,text='A different word that rhymes with "shot"').grid(row=4,column=0,sticky=W)
Label(frame5,text='A one syllable adjective').grid(row=6, column=0,sticky=W)
Label(frame5,text='A different one syllable adjective').grid(row=8,column=0,sticky=W)
Label(frame5,text='A different one syllable adjective').grid(row=10,column=0,sticky=W)

Label(frame5,text=' ').grid(row=8,column=0,sticky=W)
Label(frame5,text=' ').grid(row=9,column=0,sticky=W)
Label(frame5,text=' ').grid(row=10,column=0,sticky=W)
Label(frame5,text=' ').grid(row=11,column=0,sticky=W)

#button1 = Button(window, text = 'pain', command = print_song(one.get, two.get, three.get, four.get, five.get, six.get))
#button1.pack()

#display_area = Label(window, text ="")
#display_area.pack()

#window.mainloop()
