import random


def move():
    if key == 1:
        special_position1 = 6
        special_position2 = 7
        special_position3 = 8
        steps = 3
    elif key == 2:
        special_position1 = 0
        special_position2 = 1
        special_position3 = 2
        steps = -3 
    elif key == 3:
        special_position1 = 2
        special_position2 = 5
        special_position3 = 8
        steps = 1
    elif key == 4:
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

print("WELCOME TO MY 3X3 SLIDING PUZZLE!")
print("(u = up, d = down, l = left, r = right)")
while True:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 0
    while x % 2 != 0 or x == 0:
        x = 0
        random.shuffle(numbers)
        for number in numbers:
            for number_ahead in numbers[:numbers.index(number)]:
                if number_ahead > number:
                    x += 1
        position = numbers.index(9)
        if position == 1 or position == 3 or position == 5 or position == 7:
            x = x + 1
    numbers = [str(number) for number in numbers]
    numbers[position] = " "
    total_moves = 0
    while numbers != ['1', '2', '3', '4', '5', '6', '7', '8', ' ']:
        key = random.randint(1,4)
        move()
    print(total_moves)
    print("Yeah! You made it!\n" + "Do you want to try again?") 
    continue_choice = input("Enter r to restart or enter other key to quit:")
    if continue_choice == 'r':
        continue
    else:
        break     