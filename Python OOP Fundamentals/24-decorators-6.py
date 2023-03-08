def decorator(inner):
    def inner_decorator(*args, **kwargs):
        print(f"This function takes {len(args)} arguments")
        inner(*args)

    return inner_decorator


@decorator
def decorated(string_args):
    print(f"This happened: {str(string_args)}")


@decorator
def alsoDecorated(num1, num2):
    print(f"Sum of {str(num1)}and{str(num2)}: {str(num1 + num2)}")


if __name__ == "__main__":
    decorated("Hello")
    alsoDecorated(1, 2)
