import random


def create_numbers():
    global numbers
    global position
    numbers = [i for i in range(1,10)]
    while True:
        random.shuffle(numbers)
        x = 0
        for number in numbers:
            for number_ahead in numbers[:numbers.index(number)]:
                if number_ahead > number:
                    x += 1
        position = numbers.index(9)
        if ((position//3) + (position%3)) % 2 != 0 :
            x += 1
        if x % 2 == 0:
            numbers = [str(number) for number in numbers]
            numbers[position] = " "
            break
        else:
            continue

def move(key):
    global position
    global total_moves
    if key == 'u':
        special_positions = [i for i in range(6,9)]
        steps = 3
    elif key == 'd':
        special_positions = [i for i in range(0,3)]
        steps = -3 
    elif key == 'l':
        special_positions = [i for i in range(2,9,3)]
        steps = 1
    elif key == 'r':
        special_positions = [i for i in range(0,7,3)]
        steps = -1
    if position not in special_positions:
            temp = numbers[position + steps]
            numbers[position + steps] = numbers[position] 
            numbers[position] = temp 
            position += steps
            total_moves += 1
    else:
        print("You can't move in that way. Please try other directions.")

def show_numbers():
    for index in range(0,9,3):
        print("  ".join(numbers[index:index+3]))
    print("You total number of moves is :", total_moves)

def game_loop():
    criterion = [str(i) for i in range(1,10)]
    criterion[-1] = " "
    while numbers != criterion:
        key = input("Use'u', 'd', 'l', 'r' to move the number:")
        if key in ['u', 'd', 'l', 'r']:
            move(key)
            show_numbers()
        else:
            print("Please enter the correct letter!")
            show_numbers()
    print("Yeah! You made it!\n" + "Do you want to try again?") 



print("WELCOME TO MY '3*3' SLIDING PUZZLE!")
print("(u = up, d = down, l = left, r = right)")
while True:
    total_moves = 0
    create_numbers()
    show_numbers()
    game_loop()
    continue_choice = input("Enter r to restart or enter other key to quit:")
    if continue_choice == 'r':
        continue
    else:
        break     