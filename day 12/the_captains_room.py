def find_captain_room(k, arr):
    room_dict = {}
    for i in arr:
        if i in room_dict:
            room_dict[i] += 1
        else:
            room_dict[i] = 1
    for key, value in room_dict.items():
        if value != k:
            return key
        

if __name__ == '__main__':
    k = int(input())
    arr = list(map(int, input().split()))
    print(find_captain_room(k, arr))