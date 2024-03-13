def sort_dict_by_value(dictionary, ascending=True):
    print(dictionary.items())
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_dict

# Example dictionary
my_dict = {'a': 5, 'b': 2, 'c': 7, 'd': 1}

# Sorting in ascending order
sorted_ascending = sort_dict_by_value(my_dict)
print("Sorted in ascending order:", sorted_ascending)

# Sorting in descending order
sorted_descending = sort_dict_by_value(my_dict, ascending=False)
print("Sorted in descending order:", sorted_descending)
