def print_formatted(number):

    width = len(bin(number)[2:])
    
    for i in range(1, number +1):
        d = i
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]
        
        print(f"{d:>{width}} {o:>{width}} {h:>{width}} {b:>{width}}")