word_list = ["apple", "banana", "orange", "grape", "kiwi", "apple"]
words_to_remove = ["apple", "banana"]
filtered_list = list(filter(lambda word: word not in words_to_remove, word_list))
print("Original List:", word_list)
print("Words to Remove:", words_to_remove)
print("List after removing specific words:", filtered_list)
