def isprime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def prime(n):
    primes = []
    for i in range(2, n + 1):
        if isprime(i):
            primes.append(i)
    return primes
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    primes = prime(n)
    print("Prime numbers up to", n, "are:", primes)