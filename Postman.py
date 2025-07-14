m, cap = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(m)]
neg, pos = [], []
for x, y in orders:
    if x < 0:
        neg.append([abs(x), y])
    else:
        pos.append([x, y])
neg.sort(reverse=True)
pos.sort(reverse=True)
def go(trips):
    total = 0
    from collections import deque
    dq = deque(trips)
    while dq:
        left = cap
        d = dq[0][0]
        carry = []
        while dq and left > 0:
            p, q = dq.popleft()
            take = min(left, q)
            q -= take
            left -= take
            if q > 0:
                carry.append([p, q])
        total += 2 * d
        for c in carry:
            dq.appendleft(c)
    return total
print(go(neg) + go(pos))
