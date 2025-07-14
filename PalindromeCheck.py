def can_form_palindrome(s):
    from collections import Counter
    count = Counter(s)
    odd_chars = [c for c, v in count.items() if v % 2 != 0]
    if len(odd_chars) > 1:
        return False
    half = []
    for c, v in count.items():
        half.append(c * (v // 2))
    half_str = ''.join(half)
    center = odd_chars[0] if odd_chars else ''
    palindrome = half_str + center + half_str[::-1]
    print("One possible palindrome:", palindrome)
    return True

if __name__ == "__main__":
    s = input("Enter a string: ")
    if can_form_palindrome(s):
        print(True)
    else:
        print(False)
