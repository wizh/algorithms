def selection_sort(seq):
    for i in range(len(seq)):
        low = i

        for j in range (i + 1, len(seq)):
            if seq[j] < seq[low]:
                low = j

        seq[i], seq[low] = seq[low], seq[i]

    return seq