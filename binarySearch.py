def binarySearch(a, n, x):
   low = 0
   high = n-1
   for i in range(0, n-1):
      mid = (low + high) // 2
      if a[mid] < x:
         low = mid + 1
      elif a[mid] > x:
         high = mid - 1
      else:
         return "Element " + str(a[mid]) + " exist"
   return "Elemtent not found"

def main():
   a =  [5,1,3,8,4,6,2,9]
   while True:
      try:
         x = int(input("Input the integer you are searching for: "))
      except (ValueError, TypeError, EOFError):
         pass
      else:
         result = binarySearch(a, len(a), x)
         break
   print(result)

main()