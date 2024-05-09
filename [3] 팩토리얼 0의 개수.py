"""
<Description>
Given "N!" (the factorial of N).
Get the number of zero until it comes out the first nonzero from the back.


<Variables>
- N : natural number (0<=N<=50)

<Algorithm>
-
"""


def factorial_zero(N):
    if N == 0:  # 0! = 1
        return 0
    else:
        cnt1, cnt2 = 0, 0
        for i in range(1, N+1):
            while i % 2 == 0:
                i//=2
                cnt1 += 1
            while i % 5 == 0:
                i//=5
                cnt2 += 1
        return min(cnt1, cnt2)
print(factorial_zero(int(input())))
