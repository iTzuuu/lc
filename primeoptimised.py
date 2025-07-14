n=int(input("Enter the value of n: "))
size=(n-3)//2+1
isPrime=[True]*size
primes=[2]
def markMultiplesFalse(a):
    p=a*2+3
    for j in range(2*a**2+6*a+3, size, p):
        isPrime[j]=False
for i in range(size):
    if isPrime[i]:
        p=i*2+3
        primes.append(p)
        markMultiplesFalse(i) 
print(len(primes))               