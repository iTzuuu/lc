# A confusing number is a number that when rotated 180 degrees becomes a different valid number.
# Valid digits after rotation: 0->0, 1->1, 6->9, 8->8, 9->6

def is_confusing_number(n):
    rotate_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    s = str(n)
    rotated = []
    for ch in reversed(s):
        if ch not in rotate_map:
            return False
        rotated.append(rotate_map[ch])
    rotated_num = int(''.join(rotated))
    return rotated_num != n

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(is_confusing_number(n))
