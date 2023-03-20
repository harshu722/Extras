# printing duplication
l=["hello",10,20,40,20,60,40,30]
d=[]
for i in range(len(l)):
    for j in range(i+1,len(1)):
        if l[i]==l[j] and l[i] not in d:
            d.append(l[i])
print(d)        
