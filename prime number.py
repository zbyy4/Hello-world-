i=int(input('please enter  an integer:'))
#创建一个空list

r=list()

#添加元素2
r.append(2)

#从3开始挨个筛选
for a in range(3,i):
    xxx=False

#用a除以小于a的质数b
    for b in r:
        if a%b==0:
            xxx=False
            break
        else:
            xxx=True
    if xxx==True:
        r.append(a)
print(r)