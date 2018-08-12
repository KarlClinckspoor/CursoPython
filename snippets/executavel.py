import time
import random

while True:
    try:
        print(random.random())
        time.sleep(0.05)
    except KeyboardInterrupt:
        print('Quitting.')
        break

