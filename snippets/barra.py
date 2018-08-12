#/usr/bin/python3
import time

n = 10
for i in range(n):
    print('<' + '=' * i  + '-' * (n - i - 2) + '>\r', end='')
    time.sleep(0.3)

