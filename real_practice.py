def plusall(a):
    s = 0
    fhand1 = open("C:/Users/DELL/Desktop/score.txt",'r')
    for line in fhand1:
        i0 = line.find(a)
        i1 = line.find(" ", i0)
        if i1 == -1:
            i1 = len(line)
        s += float(line[i0+8:i1])
    fhand1.close()
    fhand2 = open("C:/Users/DELL/Desktop/result.txt",'w')
    fhand2.write("The average " + a + " score result is: " + str(s/3) + "\n")
    fhand2.close()

plusall("CSC1001")
plusall("CSC1002")
plusall("CSC1003")