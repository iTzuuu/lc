f="false"
x=int(input())
c=list(input().strip().split())
for i in range(x-1):
    for j in range(i+1,x):
        if c[i]==c[j]:
            f="true"
            break
print(f)            
    
