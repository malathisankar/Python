my_list = [1, None, 3, None, 5, None, 7, None, 9]
filtered_list = list(filter(lambda x: x is not None, my_list))
print("Original List:", my_list)
print("List after removing None values:", filtered_list)
