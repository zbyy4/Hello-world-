import random


def up():
    global position
    if position != 6 and position != 7 and position != 8:
        numbers[position], numbers[position+3] = numbers[position+3], numbers[position]
        position += 3
    else:
        print("You make a little mistake. Try again.")

def down():
    global position
    if position != 0 and position != 1 and position != 2:
        numbers[position], numbers[position-3] = numbers[position-3], numbers[position]
        position -= 3
    else:
        print("You make a little mistake. Try again.")

def left():
    global position
    if position != 2 and position != 5 and position != 8:
        numbers[position], numbers[position+1] = numbers[position+1], numbers[position]
        position += 1
    else:
        print("You make a little mistake. Try again.")

def right():
    global position
    if position != 0 and position != 3 and position != 6:
        numbers[position], numbers[position-1] = numbers[position-1], numbers[position]
        position -= 1
    else:
        print("You make a little mistake. Try again.")

def show():
    print(numbers[0:3])
    print(numbers[3:6])
    print(numbers[6:9])

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', ' ']
random.shuffle(numbers)
show()
position = numbers.index(" ")
while numbers != ['1', '2', '3', '4', '5', '6', '7', '8', ' ']:
    key = input("Use'u', 'd', 'l', 'r' to move the number:")
    if key == 'u':
        up()
        show()
    elif key == 'd':
        down()
        show()
    elif key == 'l':
        left()
        show()
    elif key == 'r':
        right()
        show()
    else:
        print("You can't do that! Please try again.")
        show()
print("Yeah! You made it!")      