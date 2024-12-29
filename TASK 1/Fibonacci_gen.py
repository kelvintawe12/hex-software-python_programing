def fibonacci_generator(limit):
    """Generates Fibonacci numbers for indefinite numbers."""
    x, y = 0, 1
    while x <= limit:
        yield x
        x, y = y, x + y

# Using the generator
fib_gen = fibonacci_generator(100)

# Iterating through the generator
for num in fib_gen:
    print(num)
