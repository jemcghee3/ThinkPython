"""Exercise 1

Repeating my advice from the previous chapter, whenever you learn a new feature, you should try it out in interactive mode and make errors on purpose to see what goes wrong.

    We’ve seen that n = 42 is legal. What about 42 = n?
    How about x = y = 1?
    In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?
    What if you put a period at the end of a statement?
    In math notation you can multiply x and y like this: x y. What happens if you try that in Python?
"""

# Exercise 2

# Practice using the Python interpreter as a calculator:

print('The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?')
radius = 5
pi = 3.1415927
volume = 4/3 * pi * radius**3
print(volume)

print('Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?')
copies = 60
cover = 24.95
wholesale = cover * .6
shipping = 3 + .75 * (copies - 1)
total_wholesale = wholesale * copies + shipping
print(total_wholesale)
print('dollars:', total_wholesale//1, 'cents:', total_wholesale % 1 * 100 // 1)

print('If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?')
start_time = 6 * 3600 + 52 * 60 # start time in seconds
easy_pace = 8 * 60 + 15 # easy pace in seconds
tempo = 7 * 60 + 12 # tempo pace in seconds
end_time = start_time + easy_pace * 1 + tempo * 3 + easy_pace * 1 # end time in seconds
hours = end_time // 3600
seconds_left = end_time % 3600
minutes = seconds_left // 60
seconds = seconds_left % 60
print('end time: ' + str(hours) + ':' + str(minutes) + f' and {seconds} seconds')