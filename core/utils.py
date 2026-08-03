def format_date(date_value):

    if isinstance(date_value, list):
        date_value = date_value[0]

    if date_value:
        return str(date_value).split()[0]

    return "Not Available"