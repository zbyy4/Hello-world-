def legal_input(number):
    # The number should be all digit and can't start with 4, 5, 6, 37.
    if number.isdigit() and len(number) > 12 and len(number) < 17:
        if number[0] in ['4','5','6'] or number[:2] == '37':
            return True

def isValid(number):
    # Count the totalSum to find out whether is it valid.
    totalSum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    if totalSum%10 == 0:
        print("Your card is valid!")
    else:
        print("Your card is invalid!")

def sumOfDoubleEvenPlace(number):
    sumOfDoubleEvenPlace = 0
    for digit in number[::-1][1::2]:
        sumOfDoubleEvenPlace += getDigit(digit)
    return sumOfDoubleEvenPlace
        
def getDigit(number):
    # add every digit
    double = int(number)*2
    if double < 10:
        return double
    else:
        return double//10 + double%10 

def sumOfOddPlace(number):
    sumOfOddPlace = 0
    for digit in number[::-1][::2]:
        sumOfOddPlace += int(digit)
    return sumOfOddPlace



while True:
    number = input("Please enter your credit card number>")
    if legal_input(number):
        break
    print("You made a input-mistake. Try again.")
isValid(number)