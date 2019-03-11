# Input
while True:
    try:
        n = int(input("Please input a positive number: "))
        if n <= 0:
            print("You made a mistake.")
            continue
        break
    except:
        print("You made a mistake.")
# Print the table.
max_length = len(str(n**(n+1)))
print("m".ljust(max_length+3) + 
      "m+1".ljust(max_length+3) + 
      "m**(m+1)".ljust(max_length+3))
for i in range(1,n+1):
    print(str(i).ljust(max_length+3) + 
          str(i+1).ljust(max_length+3) + 
          str(i**(i+1)).ljust(max_length+3))