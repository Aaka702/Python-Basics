from array import array

# Initialize the array
var = array('i', [3, 5, 2, 1, 6, 4])

# Print the original array
print("Original array:", var)

# Convert the array to a list, sort the list, and convert it back to an array
sorted_var = array('i', sorted(var))

# Print the sorted array
print("Sorted array:", sorted_var)
 