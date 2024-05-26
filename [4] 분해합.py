"""
<Description>
Put the decomposition sum of N is M. Now, M is the generator of N.
it's can be appeared to serveral generator of N. Also, there is no generator of N.
Get the minimum of generator for N.
For example, 245 is the generator of 256.


<Variables>
- N : natural number (1<=N<=1,000,000)

<Algorithm>
- Brute Force
"""

def get_generator(N):
    for i in range(N+1):
        num = i + sum(map(int, str(i)))
        if num == N:
            return i
    return 0
print(get_generator(int(input())))