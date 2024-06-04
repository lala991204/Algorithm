'''
IF you live in a-th floor, room b, you have to live with people of sum for from room 1 to room b.
Now, there are 0-th floor or higher, room 1 or higher.
And i-people live in 0-th floor, room i.

example)
1층의 3호 -> 0층: [1,1,1]
2층의 3호 -> 1층: [1,1,1] -> 0층: [3,2,1] 
3층의 6호 -> 2층: [1,1,1,1,1,1] -> 1층: [6,5,4,3,2,1] -> 0층: [21,15,10,6,3,1] (descending sum)

'''


def people_num(house):
    k, n = house[0]-1, house[1]
    cnt_list = [1]*n
    while k != 0:
        for i in range(n-1):
            cnt_list[i] = sum(cnt_list[i:])
        k -= 1
    return sum([cnt_list[i] * (i+1) for i in range(n)])


test_num = int(input())
for _ in range(test_num):
    house = []
    for _ in range(2):
        house.append(int(input()))
    print(people_num(house))
