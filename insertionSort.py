# insertion sort method

def insertionSort(a, n):
   for i in range(n):
      next = a[i]
      j =i-1
      while j>=0 and a[j] > next:
         a[j+1] = a[j]
         j -= 1
      a[j+1] = next
      
   return a

def main():
   a =  [5,1,3,8,4,6,2,9]
   result = insertionSort(a, len(a))    
   print(result)

main()