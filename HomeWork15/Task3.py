'''
Напишите функцию, которая принимает количество дней от текущей даты и
возвращает дату, которая наступит через указанное количество дней. Дополнительно,
выведите эту дату в формате YYYY-MM-DD.
'''

from datetime import datetime, timedelta


def next_date(current_date):
    """
    Returns the date that will occur after the specified number
    of days from the current date.
    :param days_from_now: The number of days from the current date.
    :return: Formatted date in the format YYYY-MM-DD.
    Examples:
    >>> next_date(666)
    '2024-09-08'
    >>> next_date(-333)
    '2024-07-30'
    """
    today = datetime.now()
    next_date = today + timedelta(days=current_date)
    formatted_next_date = next_date.strftime('%Y-%m-%d')
    return formatted_next_date


if __name__ == '__main__':
    days = 1147
    print(f'Date {days} days from now: {next_date(days)}')
