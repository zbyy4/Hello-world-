# Input
while True:
    try:
        up_bound = int(input("Please input an integer: "))
        if up_bound <= 3:
            print("You made a mistake.")
            continue
        break
    except:
        print("You made a mistake.")
# Make the prime number list.
prime_list = [2]
for number in range(3,up_bound):
    flag = False
    for prime_number in prime_list:
        if number % prime_number == 0:
            flag = False
            break
        else:
            flag = True
    if flag == True:
        prime_list.append(number)
# Print the prime number table.
bound = len(str(up_bound))
final_list = [str(prime_number).ljust(bound) for prime_number in prime_list]
for index in range(0,len(final_list),8):
    print(" ".join(final_list[index:index+8]))