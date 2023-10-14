"""
[0,0,0,0,0,0,0,0,0,0]
[3,3,3,3,3,0,0,0,0,0]
[3,3,3,10,10,7,7,7,0,0]
[3,3,3,10,10,8,8,8,1,0]

Queries:
a b k
1 5 3
4 8 7
6 9 1
"""
def array_manipulation(n, queries):
    arr = [0] * (n + 2)

    for a,b,k in queries:
        arr[a] += k
        arr[b+1] -= k
    
    maximum = temp = 0
    for value in arr:
        temp += value
        maximum = max(maximum, temp)
    return maximum
