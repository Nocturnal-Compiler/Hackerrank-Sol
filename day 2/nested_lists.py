if __name__ == '__main__':
    dic = {}
    score_list = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if score in dic:
            dic[score].append(name)
        else:
            dic[score]=[name]
        
        if score not in score_list:
            score_list.append(score)
            
    min_value = min(score_list)
    score_list.remove(min_value)
    min_value_2 = min(score_list)
        
    dic[min_value_2].sort()
    
    for i in dic[min_value_2]:
        print(i)