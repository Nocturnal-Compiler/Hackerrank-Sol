def split_and_join(line):
    presultant = line.split(" ")
    resultant = "-".join(presultant)
    return resultant

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)