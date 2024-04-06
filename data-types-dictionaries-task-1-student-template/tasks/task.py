from typing import Dict

def get_dict(s: str) -> Dict[str, int]:
    s1 = s.lower()
    result = {chr: s1.count(chr) for chr in s1}
    return result

if __name__ == '__main__':
    print(get_dict('Oh, it is python'))
