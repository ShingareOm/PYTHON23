def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Using count_upper_lower function to count upper and lower case letters in a string
string = "Hello World"
upper_count, lower_count = count_upper_lower(string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
