def minion_game(string):
    string_length = len(string)
    consonants, vowels = 0, 0 
    
    for i in range(string_length):
        if string[i] in "AEIOU":
            vowels = vowels + (string_length - i)
        else:
            consonants = consonants + (string_length - i)
            
    if consonants > vowels:
        print("Stuart",consonants)
    elif vowels > consonants:
        print("Kevin",vowels)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)