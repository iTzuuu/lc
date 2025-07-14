x=int(input())
y=int(input())
tastiness=list(map(int,input().split()))
i=0
j=y
max_tastiness=0
while j<=x:
    current_tastiness=sum(tastiness[i:j])
    if current_tastiness>max_tastiness:
        max_tastiness=current_tastiness
    i+=1
    j+=1
print(max_tastiness)
