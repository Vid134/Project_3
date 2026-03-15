# import wraps so original function metadata is preserved
from functools import wraps


def step(step_name):
    """
    Custom step decorator to print readable test steps
    """

    # decorator wrapper
    def decorator(func):

        # preserve original function name
        @wraps(func)
        def wrapper(*args, **kwargs):

            # print step start
            print(f"\nSTEP: {step_name}")

            # execute actual function
            result = func(*args, **kwargs)

            # print step completion
            print(f"STEP COMPLETED: {step_name}")

            # return function result
            return result

        return wrapper

    return decorator