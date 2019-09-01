fhand = open("C:/Users/DELL/Desktop/test.txt",'r')
counts = {}
for line in fhand:
    words = line.split()
    for w in words:
        w.replace(',','')
        w.replace('.','')
        w.replace(':','')
        w.lower()
        counts[w] = counts.get(w, 0) + 1

new_list = []

for k, v in counts.items():
    new_list.append((v,k))

new_list.sort(reverse=True)

for k,v in new_list[:20]:
    print((v,k))
