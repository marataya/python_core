
import time
import inspect

def log(fn):
    def wrapper(*args, **kwargs):
        arg_spec = inspect.signature(fn)
        params = arg_spec.parameters.keys()
        print(params)
        # Combine positional and keyword arguments
        bound_args = dict(zip(params, args))
        print(bound_args)
        str_args = ', '.join(f'{k}={v}' for k,v in bound_args.items())
        str_kwargs = ', '.join(f'{k}={v}' for k,v in kwargs.items())

        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"{fn.__name__}; args: {str_args}; kwargs: {str_kwargs}; execution time: {end - start} sec.\n")
        with open('log.txt', 'w') as f:
            f.write(f"{fn.__name__}; args: {str_args}; kwargs: {str_kwargs}; execution time: {end - start} sec.\n")
        return result
    return wrapper

@log
def foo(a, b, c):
    time.sleep(0.2)
    return a + b + c

if __name__ == '__main__':
    foo(1, 2, c=3)
