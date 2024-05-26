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

def Euclidean_algo(a, b):
    n1, n2 = max(a, b), min(a, b)
    while n1 % n2 != 0:
        tmp = n1
        n1 = n2
        n2 = tmp % n2 
    return n2, n2*(a//n2)*(b//n2)

a, b = map(int, input().split())
gcd, lcm = Euclidean_algo(a,b)
print(f"{gcd}\n{lcm}")