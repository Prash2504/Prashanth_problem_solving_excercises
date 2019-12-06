#! /usr/bin/python
# Problem : Two numbers sum i.e given a array find all pairs whose sum equal to given k

import timeit

# Using recursion
def sum_two_numbers(arr, k):
	result = []
	for i in arr:
		for j in arr[1::]:
			if (i + j) == k:
				result.append((i,j))
	return set(result)


# Using Binry search mechansim


def sum_two_k(arr, k):
	pairs = list()
	da = dict()
	for i in range(len(arr)):
		# Storing Values as keys and assigning its index value as value
		da[arr[i]] = i # takes O(n)

	for i in range(len(arr)):
		# 7 -  in {} and d[6] != 0
		if k - arr[i] in da.keys() and  da[k - arr[i]] != i:
			pairs.append((arr[i], k - arr[i]))
			pairs.append((k - arr[i], arr[i]))

	return set(pairs)


def two_sum_nlogn(a, k):
	pairs = list()
	a.sort() # sort takes O(nlogn)
	for i in range(0, len(a)):
		if a[i] <= k :
			if binary_search(a[i+1:], k - a[i]) != -1:
				pairs.append((a[i], k - a[i]))
				pairs.append((k - a[i], a[i]))
		else:
			break
	# instead of set, can also check in above if that pair exists in list before adding
	return set(pairs)  #n and total time complexity is nlogn + logn + n = nlogn


def binary_search(a, ele): # takes O(logn)
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low + high)/2
		if a[mid] == ele:
			return mid
		elif ele < a[mid]:
			high = mid - 1
		elif ele > a[mid]:
			low = mid + 1
	return -1


if __name__ == "__main__":
	arr = [1, 5, 6, 3, 2, 7, 0, 4, 55,66,77,8,7,4,3,5,6,7,8,2,1,2]
	k = 7
	print(sum_two_numbers(arr, k))
	print(timeit.timeit("two_sum_nlogn([1, 5, 6, 3, 2, 7, 0, 4, 55,66,77,8], 7)", setup="from __main__ import two_sum_nlogn", number=1))
	print(timeit.timeit("sum_two_k([1, 5, 6, 3, 2, 7, 0, 4, 55,66,77,8,7,4,3,5,6,7,8,2,1,2], 4)", setup="from __main__ import sum_two_k", number=1))

