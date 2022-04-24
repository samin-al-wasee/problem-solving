# Given a range (inclusive), find out the sum of all the even and odd fibonacci numbers in that range seperately.
# Can also be solved using the concept of perfect square.
from time import time
start = time()
def even_odd_fibonacci(start_inclusive, end_inclusive):
    prev_prev = 0
    prev = 1
    even_sum = 0
    odd_sum = 0
    while prev <= end_inclusive:
        if prev >= start_inclusive:
            if prev % 2 == 0:
                even_sum += prev
            else:
                odd_sum += prev
        nextt = prev_prev + prev
        prev_prev = prev
        prev = nextt
    return even_sum, odd_sum
print(even_odd_fibonacci(0, 20))
print("Took {taken_time} seconds".format(taken_time = time() - start))
