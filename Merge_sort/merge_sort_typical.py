from math import floor, ceil

def merge(left, right):
    merged = []

    while len(left) > 0 and len(right) > 0:
        merged += [min(left[0], right[0])]
        if left[0] <= right[0]:
            left = left[1:]
        else:
            right = right[1:]

    return merged + left + right

def merge_sort(seq):
    if len(seq) == 1:
        return seq

    return merge(merge_sort(seq[:ceil(len(seq) / 2)]),
                 merge_sort(seq[floor(len(seq) / 2):]))