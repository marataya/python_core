def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here
    """
    a, _ = map(int, a_b.split('/'))
    c, b = map(int, c_b.split('/'))

    return f'{a}/{b} + {c}/{b} = {a+c}/{b}'

if __name__ == '__main__':
    a_b = '21/55'
    c_b = '5/55'
    print(get_fractions(a_b, c_b))
    # '1/3 + 5/3 = 6/3'
