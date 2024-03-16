#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    arg = sys.argv
    number = len(arg) -1

    if number > 1:
        print("{} arguments:".format(number))
        for i in range(1, number + 1):
            print("{}: {}".format(i, arg[i]))

    elif number == 0:
        print("{} arguments.".format(number))

    else:
        print("{} argument:".format(number))
        print("{}: {}".format(number, arg[1]))
