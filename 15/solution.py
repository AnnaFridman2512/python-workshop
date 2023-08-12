def main(str):
    result = []
    # Loop over each character with its position (1-indexed)
    for index, char in enumerate(str, start=1):
        # Repeat the character, capitalize the first occurrence, and append to the result
        transformed_char = (char * index).capitalize()
        result.append(transformed_char)

    return '-'.join(result)
