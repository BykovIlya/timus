# https://acm.timus.ru/problem.aspx?space=1&num=2066


def solution(a,b,c):
    def sort(a, b, c):
        array = [int(a), int(b), int(c)]
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array[0], array[1], array[2]
    a,b,c = sort(a,b,c)
    return a-b-c if a-b-c < a-b*c else a-b*c


try:
    a = input()
    b = input()
    c = input()
    min_var = solution(a, b, c)
    print(min_var)
except Exception as e:
    print("error: ", e)