def lengoftheString(s):
    char_index_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        print("End i s", end)
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
            print("start is ",start)
        char_index_map[s[end]] = end
        print("Char inde is",char_index_map)
        max_length = max(max_length, end - start + 1)
        print("Max length is ", max_length)
    return max_length
# Test case
print(lengoftheString("pqrstuv"))  # Output: 3
