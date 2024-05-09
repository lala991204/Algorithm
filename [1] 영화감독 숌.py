"""
<Description>
Movie director Shom wants to name his movie with apocalyptic numbers.
An apocalyptic number means a number which contains successive 6 at least 3 times.
Print the nth movie name of his.

<Variables>
- n: The order of the series to know (1<=n<=10,000).

<Algorithm>
Brute Force
"""


def search_num(N):
    number = 666
    while N:
        if '666' in str(number):
            N -=1
        number +=1
    print(number-1)
search_num(int(input()))
