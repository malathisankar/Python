my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print("Original List:", my_list)
print("Filtered List (Even Numbers):", filtered_list)
