'''
<Description>
IF you live in k-th floor, room n, you have to live with people of sum for from room 1 to room n.
Now, there are 0-th floor or higher, room 1 or higher.
And i-people live in 0-th floor, room i.
For given the test case T, get the number of people lived in k-th floor, room n.

<Variables>
- T : the number of test case
- k, n : floor, room number (1 <= k, n <= 14)

<Algorithm>
- Brute Force
'''


def people_num(house):
    '''
    ex) 3층의 6호 -> 2층: [1,1,1,1,1,1] -> 1층: [6,5,4,3,2,1] -> 0층: [21,15,10,6,3,1] (descending sum)
    '''
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
