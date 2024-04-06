# https://acm.timus.ru/problem.aspx?space=1&num=2001
from sys import stdin

def solution(arr):
    arr = [int(i) for i in arr]
    return  arr[0] - arr[4], arr[1] - arr[3]


try:
    lines = []
    for line in stdin:
        lines = lines + line.split()
        if len(lines) == 6:
            break
    a, b = solution(lines)
    print(a, b)
except Exception as e:
    print("error: ", e)