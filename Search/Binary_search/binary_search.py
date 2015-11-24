def binary_search(e, l):
	lo, hi = 0, len(l)
	while lo < hi:
		mid = (lo + hi) // 2
		midval = l[mid]
		if midval < e:
			lo = mid + 1
		elif midval > e:
			hi = mid
		else:
			return mid
	return -1
