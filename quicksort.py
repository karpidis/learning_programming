def quick_sort(lista):
    """
    The function implements the Quick Sort algorithm.
    """
    # Base case: if the length of the list is less than 2, return the list as it is
    if len(lista) < 2:
        return lista
    else:
        # Pick the first element as pivot
        pivot = lista[0]
        # Create a list of elements that are less than or equal to the pivot
        less = [i for i in lista[1:] if i <= pivot]
        # Create a list of elements that are greater than the pivot
        greater = [i for i in lista[1:] if i >= pivot]
        # Recursively sort the lists 'less' and 'greater' and return the result
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Import the random module
import random
# Create an empty list 'l'
l = []
# Fill the list 'l' with 40 random integers between 1 and 20000
for i in range(40):
    l.append(random.randint(1, 20000))
    
# Print the list 'l'
print(l)
# Sort the list 'l' using the quick_sort function and print the result
print(quick_sort(l))
