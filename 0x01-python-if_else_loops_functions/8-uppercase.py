#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
<<<<<<< HEAD
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
=======
            c = chr(ord(i) - 32)
            print("{}".format(c), end="")
        else:
            print("{}".format(i), end="")
    print("")

>>>>>>> 9e12ecc0996abb44fc0d5e33702723b2d5cd22db
