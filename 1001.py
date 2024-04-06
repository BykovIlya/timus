# https://acm.timus.ru/problem.aspx?space=1&num=1001
from sys import stdin
from math import sqrt

lines = []
for line in stdin:
  lines = lines + line.split()
  
for i in range(len(lines)-1, -1, -1):
    res = sqrt(int(lines[i]))
    print('%.4f' % res)