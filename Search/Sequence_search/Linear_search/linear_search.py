def linear_search(element, seq):
    for i in range(len(seq)):
        if seq[i] == element:
            return i

    return -1