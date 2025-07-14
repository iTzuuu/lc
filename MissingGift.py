x=int(input())
gifts=list(map(int,input().split()))
counted_gifts=list(map(int,input().split()))
s1=sum(gifts)
s2=sum(counted_gifts)
missing_gift=s1-s2
print(missing_gift)