#!/usr/bin/python3
def uppercase(str):
    for caps in str:
        if ord(caps) >= 97 and ord(caps) <= 122:
            caps = chr(ord(caps) - 32)
        print("{}".format(caps), end="")
    print()
