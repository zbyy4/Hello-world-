import random


def move():
    global key
    if key == 'u':
        special_position1 = 6
        special_position2 = 7
        special_position3 = 8
        steps = 3
    elif key == 'd':
        special_position1 = 0
        special_position2 = 1
        special_position3 = 2
        steps = -3 
    elif key == 'l':
        special_position1 = 2
        special_position2 = 5
        special_position3 = 8
        steps = 1
    elif key == 'r':
        special_position1 = 0
        special_position2 = 3
        special_position3 = 6
        steps = -1
    global position
    if (position != special_position1 and 
        position != special_position2 and 
        position != special_position3):
            temp = numbers[position+steps]
            numbers[position+steps] = numbers[position] 
            numbers[position] = temp 
            position += steps
    else:
        print("You can't move in that way. Try again.")

def show():
    print(" ".join(numbers[0:3]))
    print(" ".join(numbers[3:6]))
    print(" ".join(numbers[6:9]))


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', ' ']
random.shuffle(numbers)
show()
position = numbers.index(" ")
while numbers != ['1', '2', '3', '4', '5', '6', '7', '8', ' ']:
    key = input("Use'u', 'd', 'l', 'r' to move the number:")
    if key in ['u', 'd', 'l', 'r']:
        move()
        show()
    else:
        print("Please enter the correct letter!")
        show()
        continue
print("Yeah! You made it!")      