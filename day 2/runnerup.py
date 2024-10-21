if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    standard = max(arr)
    arr_count = arr.count(standard)
    
    for i in range(arr_count):
        arr.remove(standard)
        
    print(max(arr))