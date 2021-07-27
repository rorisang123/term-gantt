"""
    Author: Rorisang Serapelo
    App name: gantt.py

    This is a module that prints a Gantt charts onto the terminal.

    INPUTS
    * Task names : list
    * Corresponding start dates : list
    * Corresponding durations : list
    NOTE: The number of items should match for the 3 lists.
"""

from colorama import Fore, init

# Constants
inactiveDay = "     "
activeDay = "▇▇▇▇"

init(autoreset=True)

# The chart function creates a Gantt chart from 3 ordered lists
def chart(tasks: list, starts: list, durations: list):
    try:
        # Error handling an empty list
        if not starts or not durations:
            raise ValueError('There should be no empty entries.')

        # Error uneven entries
        elif len(tasks) != len(starts) != len(durations):
            raise ValueError('There should be the same number of entries in the different lists.')

        # Error handling a negative entry
        isNegative = False

        for i in range(len(starts)):
            if starts[i] < 0 or durations[i] < 0:
                isNegative = True
                break

        if isNegative == True:
            raise ValueError('The start date or duration cannot be negative.')

        # Main procedure runs when data is valid
        else:
            print('                     Mon  Tue  Wed  Thur Fri  Sat  Sun')
            for k in range(len(tasks)):
                if starts[k] >= 7:
                    # If the task is not this week, just print an empty bar
                    print(Fore.GREEN, str(k + 1), '. ', _formatTaskName(tasks[k]), end='')
                    print('x' * 36)
                elif starts[k] + durations[k] > 7 :
                    # If the task continues into next week, just print what should be done of it this week
                    daysLeft = 7 - starts[k]
                    print(Fore.GREEN, str(k + 1), '. ', _formatTaskName(tasks[k]), end='')
                    print(inactiveDay*starts[k], end='')
                    print(Fore.LIGHTYELLOW_EX + activeDay*daysLeft)
                else:
                    # If the task will be started and completed this week, print it normally
                    print(Fore.GREEN, str(k + 1), '. ', _formatTaskName(tasks[k]), end='')
                    print(inactiveDay*starts[k], end='')
                    print(Fore.LIGHTYELLOW_EX + activeDay*durations[k])
    except ValueError as e:
        print(e)

# This function formats the task name when displaying it as output so the chart is well structured.
def _formatTaskName(name):
    if len(name) > 10 and len(name) != 15 :
        temp = name
        name = ''
        for k in range(7):
            name = name + temp[k]
        name = name + Fore.RED + '...' + Fore.WHITE
        for k in range(len(temp) - 4, len(temp)):
            name = name + temp[k]
        name = name + ' '
    else:
        if name != 15 :
            degree = 15 - len(name)
            name = name + (Fore.RED + '*' * degree)
    return name