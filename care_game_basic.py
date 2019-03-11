import random
your_win = 0
my_win = 0
print('Welcome to my card game.')
print("We have the same cards.\n")
print("If your card is greater than mine, it will keep comparing.")
print("And my card will dissaper.")
print("If your card is equal to mine, they will both dissapear.")
print("If your card is smaller than mine, your card will dissapear.\n")
print("But 0 is bomb! It will kill every card that meet it.")
print("At the same time, 0 will also dissapear.")
print("We all have two '0' bombs!\n")
print("Try to kill all my cards!")
print("Let's start!")
while True:
    b = [i for i in range(13)]
    b.append(0)
    a = [i for i in range(13)]
    a.insert(0,0)
    random.shuffle(b)
    c = b[:]
    d = []
    while len(b) != 0 and len(a) !=0 :
        print("Here are your left cards:",a)
        print("Your left number of cards:",len(a))
        print("My left number of cards:",len(b),"\n")
        try:
            chu = int(input("Please enter one card: "))
            if chu not in a:
                print("Please enter correct number card.")
                continue
        except:
            print("Please enter correct number card.")
            continue
        d.append(chu)
        kill_number = 0    
        while True:
            try:
                dui = b[0]
            except:
                break
            if chu != 0:
                if dui != 0 and dui < chu:
                    b.remove(dui)
                    kill_number += 1
                    continue
                elif dui == 0 or dui == chu:
                    kill_number += 1
                    b.remove(dui)
                    a.remove(chu)
                    break
                elif dui > chu:
                    a.remove(chu)
                    break
            else:
                b.remove(dui)
                a.remove(chu)
                print("You used a bomb!")
                kill_number += 1
                break    
        print("Your " + str(chu) + " killed " + str(kill_number) + " my cards.")
        continue
    if len(b) == 0:
        print("You win!")
        print("Your card play order is: ", d)
        print("My original cards list is: ",c)
        your_win += 1
    else:
        print("You lose!")
        print("Your card play order is: ", d)
        print("My original cards list is: ",c)
        print("My left cards are:",b)
        my_win += 1
    print("Your win time is: ", your_win)
    print("My win time is: ", my_win,"\n")
    print("Do you want to try again?")
    choice = input("Input 'r' to restart or other key to quit:")
    if choice == 'r':
        continue
    else:
        break