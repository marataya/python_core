from typing import List

def split(data: str, sep=None, maxsplit=-1) -> list[str]:
    """Replicates str.split function"""

    if sep is None:
        sep = " "  # Split by whitespace if no separator is provided

    result = []
    current_word = ""
    in_separator = True  # Flag to track if we're currently in a separator sequence
    idx, final_idx = 0, 0

    if maxsplit == 0:
        result = [data.strip()]
        print(result)
        return result

    if data == "":
        return []

    while idx < len(data):
        if maxsplit == 0:
            # final_idx = idx
            break
        if data[idx:idx+len(sep)] == sep:
            if not in_separator or not sep.isspace():  # Only append if not already in a separator sequence or separator is not space
                result.append(current_word)
                current_word = ""
                maxsplit -= 1
            in_separator = True  # Update flag
            idx = idx + len(sep)
        else:
            current_word += data[idx]
            in_separator = False  # Reset flag if encountering a non-separator
            idx += 1
        final_idx = idx

    # Add the last word if it exists
    if current_word or (data[final_idx-len(sep)] == sep and not sep.isspace()) and final_idx == len(data):
        result.append(current_word)
    if final_idx < len(data):
        result.append(data[final_idx:].strip())
    print(result)
    return result

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
    assert split('asdf,asdfasdf,asdf,asd', sep=',', maxsplit=2) == ['asdf', 'asdfasdf', 'asdf,asd']
    assert split('adf<>5', sep='<>', maxsplit=1) == ['adf', '5']
