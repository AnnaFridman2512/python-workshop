def main(seconds):
    # Determine if the number is negative
    is_negative = False
    if seconds < 0:
        is_negative = True
        seconds = -seconds

    # Calculate hours, minutes, and seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format the result string
    result = "{:0>1}:{:0>2}:{:0>2}".format(hours, minutes, seconds)

    # Add negative sign if the number was negative
    if is_negative:
        return "-" + result
    return result
