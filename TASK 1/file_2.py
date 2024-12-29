# Creating a generator function for iterating through a set of values
def fibonacci(limit):
    a, b = 2, 3
    while a < limit: 
        yield a       # Yield only the current value of 'a'
        a, b = b, a + b  # Update 'a' to 'b' and 'b' to the next Fibonacci number

# Use the generator function
fib_nacci = fibonacci(10)

# Iterate through the generator and print the values
for num in fib_nacci:
    print(num)

# If needed, another generator can be created like this
fn = fibonacci(20)
for num in fn:
    print(num)
