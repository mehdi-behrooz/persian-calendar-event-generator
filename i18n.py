import datetime

EPOCH = 226895

PERSIAN_MONTHS = [
    'فروردین',
    'اردیبهشت',
    'خرداد',
    'تیر',
    'مرداد',
    'شهریور',
    'مهر',
    'آبان',
    'آذر',
    'دی',
    'بهمن',
    'اسفند'
]

PERSIAN_WEEKDAYS = [
    'دوشنبه',
    'سه‌شنبه',
    'چهارشنبه',
    'پنجشنبه',
    'جمعه',
    'شنبه',
    'یکشنبه'
]

LATIN_DIGITS = '0123456789'
PERSIAN_DIGITS = '۰۱۲۳۴۵۶۷۸۹'
DIGIT_TABLE = str.maketrans(LATIN_DIGITS, PERSIAN_DIGITS)


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


def convert_digits_to_persian(number):
    return str(number).translate(DIGIT_TABLE)