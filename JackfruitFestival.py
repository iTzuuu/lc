x,y=[int(x) for x in(input().split())]
jacks=list(map(int,input().split()))
jacks.sort(reverse=True)
jam=0
for i in range(y):
    jam+=jacks[i]
print(jam)    
    