from sys import stdin

def solution(a, b):
    answer = 'yes'
    if ((a % 2 != 0) and (b % 2 == 0)):
        answer = 'no'
    return answer


try:
    lines = []
    for line in stdin:
        lines = lines + line.split()
        if len(lines) == 2:
            break
    word = solution(int(lines[0]), int(lines[1]))
    print(word)
except Exception as e:
    print("error: ", e)