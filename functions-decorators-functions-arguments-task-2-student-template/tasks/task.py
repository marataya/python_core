def union(*args) -> set:
    result = set()
    for arg in args:
        result |= set(arg)
    return result



def intersect(*args) -> set:
    if args:
        result = set(args[0])
    else:
        result = set()
    for arg in args:
        result = result.intersection(set(arg))
    return result


if __name__ == '__main__':
    print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))
    print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))
    print(intersect())
