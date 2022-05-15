def fibonacci(n):
    x = 0
    y = 1
    sum = 0
    while(sum <= n):
        print(sum)
        x = y
        y = sum
        sum = x+y
fibonacci(0)