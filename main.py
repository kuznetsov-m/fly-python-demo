import time

counter = 0

while True:
    print(f'{counter}: hello world!')
    counter += 1
    time.sleep(1)

    if counter > 200:
        assert False, "assert"