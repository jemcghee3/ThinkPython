# Exercise 2

# Start the Python interpreter and use it as a calculator.

print('How many seconds are there in 42 minutes 42 seconds?')
total_seconds =(42*60+42)
print(total_seconds)
print('How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.')
distance = (10/1.61)
print(distance)
print('If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)?')
pace_seconds = total_seconds / distance
print('minutes: ', pace_seconds // 60, 'seconds: ', pace_seconds % 60)
print('What is your average speed in miles per hour?')
speed = distance / (total_seconds / 3600)
print('mph:', speed)