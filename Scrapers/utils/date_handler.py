import dateparser


def get_date(raw_date):
    if 'astăzi' in raw_date:
        raw_date = 'azi'
    date_added = dateparser.parse(raw_date)
    return date_added
