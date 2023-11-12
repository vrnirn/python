def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(*args)
    return wrapper

@validate_args
def test(x):
    return x

print(test(5))  # Output: 5
print(test(-3))  # Output: Negative argument
print(test(3, 4))  # Output: Too many arguments
print(test('abc'))  # Output: Wrong types