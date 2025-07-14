register=0
b=int(input())
n=[[x for x in input().split()] for _ in range (b)]
s=[]
i=0
while i<b:
    if n[i][0]=="PUSH":
        s.insert(0, int(n[i][1]))
    elif n[i][0]=="STORE":
        register = s.pop(0)
    elif n[i][0]=="LOAD":
        s.insert(0, register)
    elif n[i][0]=="IFZERO":
        ch = s.pop(0)
        if ch == 0:
            i = int(n[i][1]) - 1
        else:
            s.insert(0, ch)
    elif n[i][0]=="TIMES":
        num2 = s.pop(0)
        num1 = s.pop(0)
        s.insert(0, num1 * num2)
    elif n[i][0]=="PLUS":
        num2 = s.pop(0)
        num1 = s.pop(0)
        s.insert(0, num1 + num2)
    elif n[i][0]=="DONE":
        print(s.pop(0))
        exit()
    i += 1
