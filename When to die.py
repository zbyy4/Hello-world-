name = input("What's your name?\n")
age = int(input("OK. Hello, "+name.title()+"."+"\nBy the way, how old are you?\n"))
year = 2019+100-age
message = "Sorry, "+name.title()+", you will die in year A.D. "+str(year)+"\n"
print(message)
repeat = int(input("How many times you want me to say that?\n"))
if repeat == 0:
    print("Fine. Good bye!")
if repeat > 100:
    print("I won't do that. You little asshole.")
else:
    print("If you hope so. Fine. I will do that.\n"+(message*repeat))