import time

def concatenate():
    a = ''
    for i in range(3000000):
        a += 'a'

initial = time.time()
concatenate()
end = time.time()
print(end - initial)