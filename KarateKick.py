x=int(input())
window=int(input())
maxkick=[]
kicks=list(map(int,input().split()))
maximum=0
for i in range(1,x-window+1):
    maximum=max(maximum,max(kicks[i:i+window]))
    maxkick.append(maximum)
print(maxkick)
    