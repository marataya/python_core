from functools import wraps
def validate(fn):
    '''Validates arguments'''
    def wrapper(*args, **kwargs):
        if not all(0 <= arg <= 256 for arg in args + tuple(kwargs.values())):
            return "Function call is not valid!"
        return fn(*args, **kwargs)
    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"


if __name__ == '__main__':
    print(set_pixel(0, 127, 300))
    # Function call is not valid!
    print(set_pixel(0,127,250))
    # Pixel created!
