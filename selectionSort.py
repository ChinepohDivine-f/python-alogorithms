def selectionSort(a, n):
   for i in range(n-1,0 ,-1):
      # print(i)
      max = 0
      for j in range(1,i+1):
         if a[i] > a[max]:
            min = i
      a[max], a[i] = a[i], a[max]
   
   return a

def main():
   a =  [5,1,3,8,4,6,2,9]
   result = selectionSort(a, len(a))    
   print(result)

main()



# # Selection sort in Python
# # time complexity O(n*n)
# #sorting by finding min_index
# def selectionSort(array, size):
	
# 	for ind in range(size):
# 		min_index = ind

# 		for j in range(ind + 1, size):
# 			# select the minimum element in every iteration
# 			if array[j] < array[min_index]:
# 				min_index = j
# 		# swapping the elements to sort the array
# 		(array[ind], array[min_index]) = (array[min_index], array[ind])

# arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
# size = len(arr)
# selectionSort(arr, size)
# print('The array after sorting in Ascending Order by selection sort is:')
# print(arr)


