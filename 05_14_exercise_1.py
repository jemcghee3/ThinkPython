"""Exercise 1

The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.


Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch."""

import time

current_time = time.time()
days = int(current_time // (60 * 60 * 24))
remaining = current_time % (60 * 60 * 24)
hours = int(remaining // (60 * 60))
remaining = remaining % (60 * 60)
minutes = int(remaining // 60)
remaining = remaining % 60
seconds = int(remaining // 1)

print(f'The time of day is {hours}:{minutes}:{seconds}, and it has been {days} days since the beginning of the epoch.')