def countzero(n):
    result=0
    digit=1
    while True:
        posVal,rem=divmod(n,digit)
        prefix,posVal=divmod(posVal,10)
        if prefix==0:
            return result
        if posVal==0:
            result+=(prefix-1)*digit+ rem +1
        else:
            result+=prefix*digit
        digit*=10    
x=int(input("Enter value      :"))
print(countzero(x))        