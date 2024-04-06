# https://acm.timus.ru/problem.aspx?space=1&num=2012


def solution(n):
    all_tasks = 12
    left_time = 4 * 60
    answer = 'YES'
    left_tasks = all_tasks - n
    if left_tasks * 45 > left_time:
        answer = 'NO'
    return answer


try:
    n = input().split()[0]
    word = solution(int(n))
    print(word)
except Exception as e:
    print("error: ", e)