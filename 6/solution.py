def main(bigstr, smallstr):

    def count_chars(str):

        char_count = {}


        for char in str:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count


    bigstr_count = count_chars(bigstr)

    smallstr_count = count_chars(smallstr)

    # Check if characters in smallstr can be constructed using characters from bigstr.
    for char, count in smallstr_count.items():

        # If any character in smallstr has a higher count than in bigstr, return False.
        if char not in bigstr_count or bigstr_count[char] < count:
            return False

    # If all characters in smallstr have equal or fewer occurrences in bigstr, return True.
    return True


