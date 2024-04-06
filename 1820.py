# https://acm.timus.ru/problem.aspx?space=1&num=1820

def solution(n, k):
    if (k > n):
        return 2 
    return int(n * 2 // k) + (1 if n*2 % k != 0 else 0)


try:
    n, k = input().split()
    cnt = solution(int(n), int(k))
    print(cnt)
except Exception as e:
    print("error: ", e)