def bubbleSort(a, n):
   for i in range(n-1):
      for j in range(i+1, n):
         if a[j] < a[i]:
            a[j], a[i] = a[i], a[j]
   
   return a
      
def main():
   a =  [5,1,3,8,4,6,2,9]
   result = bubbleSort(a, len(a))    
   print(result)

main()