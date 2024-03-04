# a helper function to build a max heap.
def heapify(arr, N, i):
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	
     
	if l < N and arr[largest] < arr[l]:
		largest = l

	if r < N and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapify the root.
		heapify(arr, N, largest)
# The main sort function
def heapSort(arr):
	N = len(arr)

	# Build a maxheap.
	for i in range(N//2 - 1, -1, -1):
		heapify(arr, N, i)
		
	# One by one extract elements
	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)
	return arr

_array = [4, 32.002, 4.002, 0.008, 41, 1.02, 12, 15.68, 71, 82]
print(f'\n_array: {_array}\n\nSorted array: {heapSort(_array)}')




	
