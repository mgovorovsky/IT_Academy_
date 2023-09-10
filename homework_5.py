import functools


def check_if_admin(func):
    # @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        if login != "admin":
            print("Access denied")
            return
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


login = input("enter your user type: ")


@check_if_admin
def print_account():
    print("You have 5 new messeges")


print_account()
