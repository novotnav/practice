def first_last_nr():
    b = [a[0], a[-1]]
    print (b)
    for x in b:
        print(x)
a = [6, 12, 18, 24, 30]
first_last_nr()

print(" ")

def first_last_arg():
    import sys
    first_arg = sys.argv[1]
    last_arg = sys.argv[-1]
    print(first_arg)
    print(last_arg)
first_last_arg()
