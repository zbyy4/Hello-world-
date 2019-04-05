lockers = [False]*100
# False equals closed locker. Ture equals open one.
for student_num in range(100):
    for index in range(student_num, 100, student_num+1):
        # strat point is student_num, step is student_num+1
        lockers[index] = not lockers[index]
# print out the open locker number:
n = 0
for locker in lockers:
    n += 1
    if locker:
        print("Number-" + str(n) + "-locker is open.")