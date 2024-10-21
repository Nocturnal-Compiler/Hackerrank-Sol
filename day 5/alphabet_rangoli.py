def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase[:size]
    
    lines = []
    
    for i in range(size):
        right_side = alphabet[i:size]
        left_side = alphabet[size-1:i:-1]
        line = "-".join(left_side + right_side)
        lines.append(line.center(4*size - 3, "-"))
    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)