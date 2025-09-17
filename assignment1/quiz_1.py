def print_christmas_tree(height):
    for i in range(height):
        # Print spaces + stars for tree body
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    # Print tree trunk
    print(" " * (height - 1) + "|")



def is_subsequence(x0, y0):
    i, j = 0, 0
    while i < len(x0) and j < len(y0):
        if x0[i] == y0[j]:
            i += 1
        j += 1
    return i == len(x0)


# Example usage:
print_christmas_tree(5)

print(is_subsequence("apple", "adcsjncjsppaxjjnaxle"))  # True
print(is_subsequence("apple", "bsdpple"))               # False
print(is_subsequence("apple", "paple"))                 # False
