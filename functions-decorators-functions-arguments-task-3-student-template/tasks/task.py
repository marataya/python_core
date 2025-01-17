from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    result = {}
    for arg in args:
        for k, v in arg.items():
            if k in result:
                result[k] += v
            else:
                result[k] = v
    return result

if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    print(combine_dicts(dict_1, dict_2))
    # {'a': 300, 'b': 200, 'c': 300}

    print(combine_dicts(dict_1, dict_2, dict_3))
     # {'a': 600, 'b': 200, 'c': 300, 'd': 100}
