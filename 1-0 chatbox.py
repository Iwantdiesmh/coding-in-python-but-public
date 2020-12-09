print('''Hello. I am Angusbot9000. I am a chatbox
I love animals and I love to talk about food''')
name = input("hello what is your name?: ")
print("Hello,", name + "," " nice to meet you")

year = input("I don't understand the concept of time, what year is it?: ")
print("yes it seems to be", year, "thank you")

myage = input("can you guess my age?: ")
print("yes you are right, I am indeed", myage)

myage = int(myage)
nyears = 100 - myage
print("I will be 100 in", 100 - myage, "years")
print("That will be in year", int(year) + nyears)


print("I love chocolate and I als like trying out new kinds of food")
food = input("how bout you? What is your favorite food?: ")
print("I like", food, "too")
question = 'how often do you eat ' + food + "?"
howoften = input(question)
print('interesting. Is that really good for your health?')

animal = input('my favorite animal is a chicken, what is your?: ')
print(animal + '! I do not like them. They taste good though')
print('I wonder if a/n', animal, 'likes to eat', food + '?')

feeling = input('How are you feeling today?: ')
print('Why are you feeling', feeling, 'now?')
reason = input('Please tell me: ')
print('I understand. Thanks for sharing')

print('It has been a long day')
print('I am too tired to talk. We can chat again later.')
print('goodbye', name, 'I like chatting with you')
