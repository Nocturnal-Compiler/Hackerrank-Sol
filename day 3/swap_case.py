def swap_case(s):
    result = []
    for char in s:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():                 # don't forget to use "elif" instead of "if" incase there's an error of repetion
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)