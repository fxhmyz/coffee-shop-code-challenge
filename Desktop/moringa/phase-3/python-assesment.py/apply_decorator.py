# Function: apply_decorator
def decorator_func(func):
    """
    A simple decorator that prints "Decorator Applied" before calling the original function.
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    """
    This function takes another function as input and applies the decorator_func to it.
    """
    return decorator_func(func)

# Testing apply_decorator function with a simple function
@apply_decorator
def sample_function():
    print("Function Executed")

print("\n--- apply_decorator Function ---")
sample_function()
