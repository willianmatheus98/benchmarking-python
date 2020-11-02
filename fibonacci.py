import time

def fibonacci(x):
    a, b = 0, 1
    n = 0
    while n < x: 
        a, b = b, a + b 
        n += 1
    return a 

inicio = time.time()
for i in range(0, 300000):
    fibonacci(400)
fim = time.time()
print(fim - inicio)