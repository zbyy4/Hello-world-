import random


def queen(A, pos=0):
    global total_solutions
    if pos == N:
        solution = A[:]
        total_solutions.append(solution)
        return
    for col in range(N):
        A[pos], flag = col, True
        for row in range(pos):
            if A[row] == col or abs(col - A[row]) == pos - row:
                flag = False
                break
        if flag:
            queen(A, pos+1)

def print_queens(total_solutions):
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
queen([0]*N)
print_queens(total_solutions)