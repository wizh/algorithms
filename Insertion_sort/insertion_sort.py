def insertion_sort(n):
    for i in range(1, len(n)):
        for j in range(i, 0, -1):
            if n[j - 1] < n[j]:
                break
            n[j - 1], n[j] = n[j], n[j - 1]

    return n