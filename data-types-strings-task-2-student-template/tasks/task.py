def get_longest_word(s: str) -> str:
    """
     Add your code here
    """

    words = s.split()
    max_len = 0
    max_el_idx = 0
    for i in range(0, len(words)):
        if max_len < len(words[i]):
            max_len = len(words[i])
            max_el_idx = i
    return words[max_el_idx]


if __name__ == '__main__':
    print(get_longest_word('Python is simple and effective!'))
    print(get_longest_word('Any pythonista like namespaces a lot.-pythonista'))
