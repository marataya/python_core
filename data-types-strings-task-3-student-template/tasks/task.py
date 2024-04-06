def replacer(s: str) -> str:
    """
    Add your code here
    """
    result = ""
    for chr in s:
        if chr == "'":
            result += '"'
        elif chr == '"':
            result += "'"
        else:
            result += chr
    return result

if __name__ == '__main__':
    print(replacer('''Test's string \"ahah\"'''))

