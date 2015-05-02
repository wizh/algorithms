def bubble_sort(seq):
    for i in range(len(seq)):
        swapped = False

        for j in range(len(seq) - i-1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                swapped = True

        if not swapped:
            break
    return seq