#!/usr/bin/python3
def magic_string(magic=[]):
    magic += ['BestSchool']
    return str(magic)[1:-1].replace("'", "")
