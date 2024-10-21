if __name__ == '__main__':
    N = int(input())
    arr = [] # make sure to declare this
    for i in range(N):
        action = input().split()
        
        if action[0] == "insert":
            arr.insert(int(action[1]), int(action[2])) # 1 acts as e, 2 acts as i
        elif action[0] == "print":
            print(arr)
        elif action[0] == "remove":
            arr.remove(int(action[1]))
        elif action[0] == "append":
            arr.append(int(action[1]))
        elif action[0] == "sort":
            arr.sort()
        elif action[0] == "pop":
            arr.pop()
        elif action[0] == "reverse":
            arr.reverse() # for furture refrence, arr = arr.reverse() isn't needed