def solution(a, b):
    max = 10
    sum = 0
    if a + b > max:
        sum = 10
    else:
        sum = a + b - 1
    return sum - a, sum - b

try:
    a,b = input().split()
    c, d = solution(int(a), int(b))
    print(c, d)
except Exception as e:
    print("error: ", e)