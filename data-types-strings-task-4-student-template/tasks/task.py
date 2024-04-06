import re


def check_str(s: str):
    """
    Add your code here
    """
    sanitized_str = re.sub(pattern=r'[^a-z0-9]', repl='', string=s.lower())
    return sanitized_str == sanitized_str[::-1] and len(sanitized_str) != 0

if __name__ == '__main__':
    print(check_str("A dog! A panic in a pagoda!"))
    print(check_str("Do nine men Interpret? Nine men I nod"))
    print(check_str("T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt upset on drab pot toilet."))
    print(check_str("A man, a plan, a canal — Panama!"))
    print(check_str("32635745"))
    print(check_str("12321"))
