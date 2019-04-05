import random


def queen(A, pos=0):  # Position test start from the first place.
    global total_solutions
    if pos == N:  # If the test gets to the last position
        solution = A[:]
        total_solutions.append(solution)  # Pick this solution out.
        return
    for col in range(N):
        A[pos], flag = col, True
        for row in range(pos):
            if A[row] == col or abs(col - A[row]) == pos - row:
                # Queens can't in the same col, row and diagonal.
                flag = False
                break
        if flag:
            # If ture, move to the next position test.
            queen(A, pos+1)
            # If false, the test will back to the former place to continue. 

def print_queens(total_solutions):
    # From the total_solutions we randomly choose one to print out.
    number = random.randint(0,len(total_solutions)-1)
    random_output = total_solutions[number]
    for col in random_output:
        for position in range(N):
            if col == position:
                print("|Q", end = "")
            else:
                print("| ", end = "")
        print("|")    

N = 8
total_solutions = []
queen([0]*N) # N elements.
print_queens(total_solutions)