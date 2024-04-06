# https://acm.timus.ru/problem.aspx?space=1&num=1264
def solution(n, m):
    cnt = n * (m + 1)
    return cnt


try:
    a,b = input().split()
    c = solution(int(a), int(b))
    print(c)
except Exception as e:
    print("error: ", e)