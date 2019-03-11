import random


def enter_n():
    while True:
        try:
            n = int(input("Please enter a number n:"))
            if n < 2:
                print("The number is too small.")
                continue
            max_length = len(str(n**2))+2
            return n, max_length
        except:
            print("You made a mistake.Try again.")
            continue

def create_numbers():
    global numbers
    global position
    numbers = [i for i in range(1,n**2+1)]
    while True:
        random.shuffle(numbers)
        x = 0
        for number in numbers:
            for number_ahead in numbers[:numbers.index(number)]:
                if number_ahead > number:
                    x += 1
        position = numbers.index(n**2)
        if ((position//n) + (position%n)) % 2 != 0 :
            x += 1
        if x % 2 == 0:
            numbers = [str(number).ljust(max_length) for number in numbers]
            numbers[position] = " ".ljust(max_length)
            break
        else:
            continue

def move(key):
    global position
    global total_moves
    if key == 'u':
        special_positions = [i for i in range(n**2-n,n**2)]
        steps = n
    elif key == 'd':
        special_positions = [i for i in range(0,n)]
        steps = -n 
    elif key == 'l':
        special_positions = [i for i in range(n-1,n**2,n)]
        steps = 1
    elif key == 'r':
        special_positions = [i for i in range(0,n**2-2,n)]
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
    for index in range(0,n**2,n):
        print("  ".join(numbers[index:index+n]))
    print("You total number of moves is :", total_moves)

def game_loop():
    criterion = [str(i).ljust(max_length) for i in range(1,n**2+1)]
    criterion[-1] = " ".ljust(max_length)
    while numbers != criterion:
        key = input("Use'u', 'd', 'l', 'r' to move the number:")
        if key in ['u', 'd', 'l', 'r']:
            move(key)
            show_numbers()
        else:
            print("Please enter the correct letter!")
            show_numbers()
    print("Yeah! You made it!\n" + "Do you want to try again?") 



print("WELCOME TO MY 'N*N' SLIDING PUZZLE!")
print("(u = up, d = down, l = left, r = right)")
while True:
    n, max_length = enter_n()
    total_moves = 0
    create_numbers()
    show_numbers()
    game_loop()
    continue_choice = input("Enter r to restart or enter other key to quit:")
    if continue_choice == 'r':
        continue
    else:
        break     