import os
from colored import fg, attr
from schedule import Schedule


def color_word(color, word):
    return fg(color) + word + attr('reset')


if __name__ == '__main__':
    cal = Schedule()
    display = cal.make_calendar()

    while True:

        print(display)
        command = input("Input: ")

        if command == '.calendar':
            display = cal.make_calendar()

        elif command == ".week":
            cal.next_week()
            display = cal.make_calendar()

        elif command.split()[0] == ".month":

            month = command.split()[1].upper()
            month_list = cal.month_list
            if month in month_list:
                cal.view_month(month_list.index(month))
                display = cal.make_calendar()

        elif command == ".help":
            display = f"""
{color_word('light_green', '.calendar')}: changes display to the calendar
    {color_word('light_green', '.week')}: proceeds to the next week
    {color_word('light_green', '.month')} {color_word('red', '[month name]')}: view [month name]

            """

        os.system('cls')
