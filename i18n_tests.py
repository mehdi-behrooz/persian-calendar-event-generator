import i18n

def main():
    
    date = i18n.to_gregorian(1400, 1, 1)
    assert date.year == 2021
    assert date.month == 3
    assert date.day == 21

    year, month, day = i18n.to_jalali(date)
    assert year == 1400
    assert month == 1
    assert day == 1

    assert i18n.convert_digits_to_persian(42390) == "۴۲۳۹۰"


if __name__ == '__main__':
    main()