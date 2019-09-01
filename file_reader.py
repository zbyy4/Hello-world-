filename = 'programming.txt'

with open(filename, 'r') as file_object:
    msg = file_object.read(5)
print(msg)