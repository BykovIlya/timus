# https://acm.timus.ru/problem.aspx?space=1&num=1787

def solution(k, n, arr):
    k = int(k)
    n = int(n)
    arr = [int(i) for i in arr][:n]
    curr_cnt = 0
    for car in arr:
        curr_cnt = curr_cnt + (car - k)
        curr_cnt = curr_cnt if curr_cnt > 0 else 0
    return curr_cnt


try:
    k, n = input().split()
    arr = input().split()
    cnt = solution(k, n , arr)
    print(cnt)
except Exception as e:
    print("error: ", e)