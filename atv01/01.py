def sort_and_find_extremes(lst):
    # Convert numeric strings to float
    lst = [ float(x) if isinstance(x, str) else x for x in lst]
    
    # Sort the list in descending order
    lst.sort(reverse=True)
    
    # Return the ordered list, smallest and largest value
    return lst, min(lst), max(lst)

# Results
lista = [9, 2, 95, 28, 0, 73, 81, 91, 71, '22', 6, 21, 1, 47, "52", 35, 68, 29, 66, 91, 81, "99", 40]
sorted_list, min_val, max_val = sort_and_find_extremes(lista)
print("Lista Ordenada:", sorted_list)
print("Menor Valor:", min_val)
print("Maior Valor:", max_val)
