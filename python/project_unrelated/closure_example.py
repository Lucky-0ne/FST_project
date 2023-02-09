# In this example, the inner_function is a closure because it remembers the value of x in the enclosing scope, even though outer_function has finished execution.
# When we call closure(5), it returns the sum of 5 and the remembered value of x, which is 10.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)

print(closure(5))

# Output: 15