def find_duplicates(arr):
    hash_table = {}  # Initialize an empty hash table
    duplicates = []  # Store found duplicates

    for num in arr:
        if num in hash_table:
            duplicates.append(num)  # Add duplicate to the list
        else:
            hash_table[num] = True  # Insert the element in the hash table

    return duplicates

# Test the function
print(find_duplicates([1, 2, 3, 2, 4, 3]))  # Output: [2, 3]
