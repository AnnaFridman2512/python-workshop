def main(names_string):
    email_counter = {}
    result = []

    # Split the names_string into a list of names
    names_list = [name.strip() for name in names_string.split(",")]

    for name in names_list:
        # Extract the first and last names
        individual_names = name.split()
        first_name, last_name = individual_names[0], individual_names[-1]

        # Remove non-alpha characters from first and last names
        clean_first = ''.join(filter(str.isalpha, first_name))
        clean_last = ''.join(filter(str.isalpha, last_name))

        # Create the initial email
        email = f"{clean_first}.{clean_last}@company.com".lower()

        # Handle uniqueness with counters
        if email in email_counter:
            email_counter[email] += 1
            email = email.replace("@company.com", f"{email_counter[email]}@company.com")
        else:
            email_counter[email] = 1

        result.append((name, email))

    return result

