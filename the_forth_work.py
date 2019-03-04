import random


def move():
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
    global total_moves
    if (position != special_position1 and 
        position != special_position2 and 
        position != special_position3):
            temp = numbers[position + steps]
            numbers[position + steps] = numbers[position] 
            numbers[position] = temp 
            position += steps
            total_moves += 1
    else:
        print("You can't move in that way. Try again.")

def show():
    print(" ".join(numbers[0:3]))
    print(" ".join(numbers[3:6]))
    print(" ".join(numbers[6:9]))
    print("You total number of moves is :", total_moves)


while True:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        random.shuffle(numbers)
        x = 0
        for number in numbers:
            for number_ahead in numbers[:numbers.index(number)]:
                if number_ahead > number:
                    x += 1
        position = numbers.index(9)
        if position == 1 or position == 3 or position == 5 or position == 7:
            x += 1
        if x % 2 == 0:
            numbers = [str(number) for number in numbers]
            numbers[position] = " "
            break
        else:
            continue
    total_moves = 0
    show()
    while numbers != ['1', '2', '3', '4', '5', '6', '7', '8', ' ']:
        key = input("Use'u', 'd', 'l', 'r' to move the number:")
        if key in ['u', 'd', 'l', 'r']:
            move()
            show()
        else:
            print("Please enter the correct letter!")
            show()
            continue
    print("Yeah! You made it!\n" + "Do you want to try again?") 
    continue_choice = input("Enter y to restart or enter other key to quit:")
    if continue_choice == 'y':
        continue
    else:
        break     