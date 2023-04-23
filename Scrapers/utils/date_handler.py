import dateparser


def get_date(raw_date):
    if 'astăzi' in raw_date:
        raw_date = raw_date.replace('astăzi', 'azi')
    date_added = dateparser.parse(raw_date)
    # Add a unique microseconds value to the datetime object
    microseconds = len(str(date_added.microsecond))
    print(microseconds)
    unique_microseconds = int(str(date_added.microsecond) + '0'*(6-microseconds))
    unique_date_added = date_added.replace(microsecond=unique_microseconds)
    print(unique_date_added)
    return unique_date_added

