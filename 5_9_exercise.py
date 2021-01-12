def print_n(s, n):
    print('print_n', 'n -->', n)
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

s = 'Hello!'
n = 2
print('__main___', '')

print_n(s, n)

def do_n(f, n):
    f()
    f()

def print_1():
    print('Hello!')

do_n(print_1, 2)