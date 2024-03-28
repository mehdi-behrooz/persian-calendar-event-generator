import datetime

EPOCH = 226895

def to_gregorian(year, month, day):
    """Returns a date object corresponding to a specified Persian date."""
    k = EPOCH - 1
    k += 365 * (year - 1)
    k += (8 * year + 21) // 33
    if month <= 7:
        k += 31 * (month - 1)
    else:
        k += 30 * (month - 1) + 6
    k += day

    return datetime.date.fromordinal(k)


def to_jalali(date):
    """Returns a tuple of year, month, and day for a specified
    datetime object."""
    if isinstance(date, datetime.datetime):
        date = date.date()
    year = (33 * (date.toordinal() - EPOCH) + 3) // 12053 + 1
    day = (date - to_gregorian(year, 1, 1)).days
    if day < 216:
        month = day // 31 + 1
        day = day % 31 + 1
    else:
        month = (day-6) // 30 + 1
        day = (day-6) % 30 + 1
    
    return (year, month, day)


