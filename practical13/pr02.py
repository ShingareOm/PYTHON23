def concatenate_strings(string1, string2):
    # Using the + operator
    concatenated_string1 = string1 + string2

    # Using str.join() method
    concatenated_string2 = ''.join([string1, string2])

    return concatenated_string1, concatenated_string2

# Example usage:
string1 = "Hello"
string2 = "World"

concatenated_string1, concatenated_string2 = concatenate_strings(string1, string2)
print("Concatenated string using + operator:", concatenated_string1)
print("Concatenated string using str.join() method:", concatenated_string2)
