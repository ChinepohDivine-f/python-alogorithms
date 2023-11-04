# insertion sort method

def insertionSort(a, n):
   for i in range(n):
      next = a[i]
      j =i-1
      for j in range(i-1,0, -1):
         if j>=0 and a[j]:
            a[j+1] = a[j]
      a[j+1] = next

def main():
   a =  [5,1,3,8,4,6,2,9]
   result = insertionSort(a, len(a))    
   print(result)

main()