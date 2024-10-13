'''
Напишите скрипт, который получает текущее время и дату, а затем выводит их в
формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
недели в году
'''

from datetime import datetime


def format_datetime():
    """Displays the current time and date in
    the format YYYY-MM-DD HH:MM:SS.
    Additionally, print the day of the week and the number"""
    time_now = datetime.now()
    date_format = time_now.strftime('%Y-%m-%d %H:%M:%S')
    day_week = time_now.strftime('%A')
    week_number = time_now.isocalendar()[1]
    print(f'Current date and time: {date_format}\n'
          f'Day of the week: {day_week}\n'
          f'Week number: {week_number}')


if __name__ == '__main__':
    format_datetime()
