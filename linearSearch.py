# Linear Search ( Array A, Value x)
# Step 1: Set i to 1
# Step 2: if i > n then go to step 7
# Step 3: if A[i] = x then go to step 6
# Step 4: Set i to i + 1
# Step 5: Go to Step 2
# Step 6: Print Element x Found at index i and go to step 8
# Step 7: Print element not found
# Step 8: Exit
# Pseudocode
# procedure linear_search (list, value)
# for each item in the list
# if match item == value
# return the item‟s location
# end if
# end for
# end procedure


def linearSearch(a, x, n):
   for i in range(0,n):
      if a[i] == x:
         return "Print element " + str(x) + " Found at index " + str(i)
      
def main():
   a = [5,1,3,8,4,6,2,9]
   while True:
      try:
         x = int(input("Input the integer you are searching for: "))
      except (ValueError, TypeError, EOFError):
         pass
      else:
         result = linearSearch(a, x, len(a))
         break
   if result == None:
      print("Element not found")
   else:
      print(result)
   
if __name__ == "__main__":
   main()