def format_string(num, char):
    formatted_string = "{:04}{}".format(num, char)
    return formatted_string

# Test the function with arguments 145 and 'o'
result = format_string(145, 'o')
print(result)
