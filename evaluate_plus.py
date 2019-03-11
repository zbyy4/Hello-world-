def evaluate(e):
    s = 0
    sIndex = 0
    flag = False
    while True:
        eIndex = e.find("+", sIndex)
        if eIndex == -1:
            flag = True
            eIndex = len(e)
        num = int(e[sIndex:eIndex])
        s += num
        sIndex = eIndex + 1
        if flag: break
    return s
        
print(evaluate("11+22+33"))