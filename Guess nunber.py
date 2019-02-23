import random
number = random.randint(0,20)
print("Can you guess how old am I?")
guess = int(input("Please enter you answer(between 0 and 20): "))
while guess != number:
    if guess > number:
        print("It's too big!")
        guess = int(input("Please enter you answer again: "))
    elif guess < number:
        print("It's too small!")
        guess = int(input("Please enter you answer again: "))
print("Yes! I'm "+str(number)+" years old.")