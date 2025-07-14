x = int(input())
anagrams = input().split()
groups = {}
for word in anagrams:
    key = ''.join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
for group in groups.values():
    print(' '.join(group))