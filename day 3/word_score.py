def score_words(words):
    vowels = "aeiouy"
    score = 0
    
    for word in words:
        num_vowels = 0
        
        for char in word:
            if char in vowels:
                num_vowels += 1
                
        if num_vowels % 2 == 0:
            score += 2
            
        else:
            score += 1
            
    return score

if __name__ == '__main__':
    n = int(input())
    words = input().split()  
    print(score_words(words))
