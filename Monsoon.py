x=int(input())
building=[[int(x) for x in input().split()] for _ in range (x)]
r=0
i=0
while i < x:
    r+=1
    x1,y1=building[i]
    j=i+1
    while j<x:
        x2,y2=building[j]
        if abs(x2-x1)<=y1-y2:
            j+=1
        elif abs(x2-x1)<=y2-y1:
            i=j
            x1,y1=x2,y2
            j+=1
        else:
            break
    i=j
print(r)    