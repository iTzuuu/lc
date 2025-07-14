n = int(input("Enter the value of n: "))
if n < 2:
    print("Prime numbers up to", n, "are: []")
else:
    list1 = [True] * (n + 1)
    list1[0] = list1[1] = False
    for i in range(4, n + 1, 2):
        list1[i] = False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if list1[i]:
            for j in range(i * i, n + 1, 2 * i):
                list1[j] = False
    primes = [2] + [i for i in range(3, n + 1, 2) if list1[i]] if n >= 2 else []
    print("Prime numbers up to", n, "are:", primes)