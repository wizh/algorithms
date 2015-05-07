def quicksort(seq, low, high):
    if low < high:
        pivot = partition(seq, low, high)
        quicksort(seq, low, pivot)
        quicksort(seq, pivot + 1, high)

    return seq

def partition(seq, low, high):
    pivot = seq[low]
    leftwall = low

    for i in range(low + 1, high):
        if seq[i] < pivot:
            leftwall += 1
            seq[leftwall], seq[i] = seq[i], seq[leftwall]

    seq[low], seq[leftwall] = seq[leftwall], seq[low]

    return leftwall

import random
l = random.sample(range(1000), 1000)

print(quicksort(l, 0, len(l)))