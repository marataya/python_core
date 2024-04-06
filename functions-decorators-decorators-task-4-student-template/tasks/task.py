from functools import wraps
def decorator_apply(lambda_func):
    '''Accepts lambda and returns a decorator that applies that lambda to result of wrapped func'''
    def decorator(decorated_func):
        @wraps(decorated_func)
        def wrapper(*args, **kwargs):
            result = decorated_func(*args, **kwargs)
            return lambda_func(result)
        return wrapper
    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num


if __name__ == '__main__':
    print(return_user_id(42))
