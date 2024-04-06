def solution(n):
    word = ''
    dict = [[1, 4, 'few'],
            [5, 9, 'several'],
            [10, 19, 'pack'],
            [20, 49, 'lots'],
            [50, 99, 'horde'],
            [100, 249, 'throng'],
            [250, 499, 'swarm'],
            [500, 999, 'zounds'],
            [1000, 2001, 'legion']]
    
    for pair in dict:
        if ((n >= pair[0]) and (n <= pair[1])):
            word = pair[2]
    return word

try:
    n = input().split()[0]
    word = solution(int(n))
    print(word)
except Exception as e:
    print("error: ", e)

