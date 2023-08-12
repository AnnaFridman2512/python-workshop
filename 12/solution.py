import re
from collections import Counter

def main(logfile):
    status_counter = Counter() #Counts numer of appearances in list and creates dict {value: number_of_appearances"

    # Regular expression pattern to match the status code in each log entry.
    pattern = r'HTTP/1\.0" (\d{3}) '

    with open(logfile, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                status = int(match.group(1)) # Extract the status code from the match.
                status_counter[status] += 1

    # Sort the Counter by values (counts) in descending order and convert to a list of tuples.
    sorted_statuses = sorted(status_counter.items(), key=lambda x: x[1], reverse=True)
    #key=lambda x: x[1] part is telling Python to sort these tuples
    # based on the second item, which is the count.
    # reverse=True ensures that the sort is in descending order.
    return sorted_statuses

