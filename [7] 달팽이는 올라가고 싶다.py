'''
<Description>
There is the snail and the wooden stick.
During the day, it could climb as much as A.
At night, it might slip as much as B during sleeping.
(If it arrive at the peak, it can't slip anymore.)
Now, how much the days if it arrive at the peak?

<Variables>
- A : the length the snail could climb during the day
- B : the length the snail might slip at night
- V : the length of the wooden stick
(1 ≤ B < A ≤ V ≤ 1,000,000,000)

<Algorithm>
- Brute Force

'''

def snail_count(A, B, V):
    '''
    (A-B)*n >= (V-A) => n >= (V-A)//(A-B)

    '''
    if (V-A)%(A-B) == 0:
        return (V-A)//(A-B) + 1
    else:   
        return (V-A)//(A-B) + 2

A, B, V = map(int, input().split())
print(snail_count(A, B, V)) 
