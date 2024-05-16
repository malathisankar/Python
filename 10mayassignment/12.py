from functools import reduce
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1]) if n > 1 else [0]
n = 10
print("Fibonacci series up to", n, ":", fibonacci_series(n))
