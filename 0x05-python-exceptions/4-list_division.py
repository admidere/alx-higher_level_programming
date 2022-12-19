#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divide = 0
    new_list = []
    for i in range(list_length):
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            divide = 0
            print("wrong type")
        except ZeroDivisionError:
            divide = 0
            print("division by 0")
        except IndexError:
            divide = 0
            print("out of range")
        finally:
            new_list.append(divide)
    return(new_list)
