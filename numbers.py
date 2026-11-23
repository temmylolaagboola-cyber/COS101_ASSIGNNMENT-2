
def list_sum(numbers):
    """Return the sum of all numbers in the list."""
    total = 0  
    for n in numbers:
    total += n

def list_mean(numbers):
    """Return  the average (mean) of the numbers in the list."""
    if not numbers:
       return None
    return list_sum(numbers)/len(numbers)

def median_and_mode(numbers):
    """Return(median,modes).modes is a list because there can be ties."""
    if not numbers:
       return None,[]
   
    # Median: middle values of the sorted list
    s= sorted(numbers)
    mid =lens(s)//2
    if len(s)%==1:
        median =s[mid]
    else:
         median = (s[mid -1] +s[mid]) /2

    # mode: the value(S) that appears most often
    counts = {}
    for n in numbers:
        counts{n} = counts.get(n,0)+ 1
   highest = max(counts.values())
   modes = [n for n,c in counts.items() if c ==highest]
   return median,modes

   # Test with the given numbers
   my_numbers =[2,3,5,7,8,4,5,3,2,9,6,3,8,5,3,4,2,3,9,4,3]
  
  
print("Sum:",list_sum(my_numbers))
print("Mean:",list_mean(my_numbers))
median,modes= median_and_mode(my_numbers)
print("median:",median)
print("mode:",modes)