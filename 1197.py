# https://acm.timus.ru/problem.aspx?space=1&num=1197

from sys import stdin

def solution(n, arr):
    n = int(n)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    arr = [str(letters.index(i[0])) + i[1] for i in arr]
    res = []
    for i in arr:
        a = int(i[0])
        b = int(i[1])
        if a * b <= 1 or a * b >= 64:
            res.append(2)
        elif a * b <= 2 or a * b >= 56:
            res.append(3)

    return 0

try:
    lines = []
    n = input()
    for line in stdin:
        lines = lines + line.split()
        if len(lines) == int(n):
            break
    print(n, lines)
    cells = solution(n, lines)

except Exception as e:
    print("error: ", e)