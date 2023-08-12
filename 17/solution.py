import re

def main(txt):
    #Extract emails from text
    email_pattern = re.compile(r'[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+')
    emails = re.findall(email_pattern, txt)

    #Remove duplicates (using dictionary to preserve order)
    email_dict = {}
    for email in emails:
        lower_email = email.lower()
        if lower_email not in email_dict:
            email_dict[lower_email] = email

    # Step 3: Sort emails by domain and then by name
    sorted_emails = sorted(email_dict.values(), key=lambda x: (x.split('@')[1], x.split('@')[0]))

    return sorted_emails
