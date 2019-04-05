def sqrt(n):
    lastGuess = 1
    while True:
        nextGuess = (lastGuess + (n/lastGuess))/2
        if abs(nextGuess-lastGuess) < 0.0001:
            return nextGuess
        lastGuess = nextGuess

n = eval(input("Please input a positive number>"))
print(sqrt(n))