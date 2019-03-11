import random


def create_numbers():
    # Generate a solvable 8-puzzle.
    global numbers
    global position
    numbers = [i for i in range(1,10)]
    while True:
        random.shuffle(numbers)
        x = 0  # x is the parity of the permutation of all 9 numbers.
        for number in numbers:
            for number_ahead in numbers[:numbers.index(number)]:
                if number_ahead > number:
                    x += 1
        position = numbers.index(9)
        if ((position//3) + (position%3)) % 2 != 0 :
            x += 1
        if x % 2 == 0:  # When x is even, then the puzzle is solvable.
            numbers = [str(number) for number in numbers]
            numbers[position] = " "
            break

def show_numbers():
    # Print the puzzle.
    for index in range(0,9,3):
        print("  ".join(numbers[index:index+3]))

def test_direction():
    # Prompt further direction.
    if position == 0:
        further_directions = " (up, left) "
    elif position == 1:
        further_directions = " (up, left, right) "
    elif position == 2:
        further_directions = " (up, right) "
    elif position == 3:
        further_directions = " (up, down, left) "
    elif position == 4:
        further_directions = " (up, down, left, right) "
    elif position == 5:
        further_directions = " (up, down, right) "
    elif position == 6:
        further_directions = " (down, left) "
    elif position == 7:
        further_directions = " (down, left, right) "
    else:
        further_directions = " (down, right) "
    return further_directions

def move(key):
    # Move the number and count total moves.
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
            # To avoid a long line, here use temp to exchange the position.
            temp = numbers[position + steps]
            numbers[position + steps] = numbers[position] 
            numbers[position] = temp 
            position += steps
            total_moves += 1
    else:
        print("You can't move in that way.")

def game_loop():
    # Control the game process.
    criterion = [str(i) for i in range(1,10)]
    criterion[-1] = " "  # "criterion" list is the final goal.
    while numbers != criterion:  # Determine when to stop.
        further_directions = test_direction()
        key = input("Input sliding direction" + further_directions + ">")
        if key in ['u', 'd', 'l', 'r']:
            move(key)
            show_numbers()
        else:
            print("Please enter the correct letter!")
            show_numbers()
    print("Congratulations! " +
          "You solved the puzzle in " + 
          str(total_moves) + " moves!") 


print("WELCOME TO MY '3*3' SLIDING PUZZLE!")
print("(u = up, d = down, l = left, r = right)")
while True:
    total_moves = 0
    create_numbers()
    show_numbers()
    game_loop()
    continue_choice = input("Enter r to restart or enter other key to quit:")
    if continue_choice != 'r':
        break