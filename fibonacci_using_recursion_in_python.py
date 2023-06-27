# creating the function for returning elements of the fibonacci series
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  #recursive call to the function

# Testing the fibonacci function
for i in range(10):
    print(fibonacci(i))
