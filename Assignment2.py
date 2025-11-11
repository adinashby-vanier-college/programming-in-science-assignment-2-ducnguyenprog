# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
   numbers.sort(reverse = True)

   if len(numbers) == 0:
       return (None, None)
   
   if len(numbers) == 1:
       return (numbers[0], None)

   max1 = numbers[0]
   max2 = None

   for n in numbers[1:]:
       if n < max1:
           max2 = n
           break

   return max1, max2

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique_list = list(set(numbers))
    unique_list.sort()

    return unique_list
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    cumulative = [sum(arr[:i + 1]) for i in range(len(arr))]

    return cumulative
# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed = [[0 for i in range(rows)] for i in range(columns)]

    for j in range(rows):
        for k in range(columns):
            transposed[k][j] = matrix[j][k]

    return transposed
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):

    if step <= 0:
        return("Step value must be positive")
    
    return [lst[i] for i in range(0, len(lst), step)]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):

    if len(list1) != len(list2):
        return("The lists must be of equal length")
    
    result = 0

    for i in range(len(list1)):
        result += list1[i] * list2[i]

    return result

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    return [[0, 0], [0, 0]]


print(max_two_in_list([1, 3, 2, 5, 5]))


5, 5, 3, 2, 1