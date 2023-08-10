def main(word, parts):
    # Convert the comma-separated string into a list
    parts_list = parts.split(',')

    # Iterate through the word to find a split where both parts exist in parts_list
    for i in range(1, len(word)):
        first_part = word[:i]
        second_part = word[i:]

        # Handle case where both parts are the same
        if first_part == second_part:
            if parts_list.count(first_part) >= 2:
                return [first_part, second_part]
        elif first_part in parts_list and second_part in parts_list:
            return [first_part, second_part]

    return []