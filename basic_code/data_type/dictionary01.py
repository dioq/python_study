#!/usr/bin/python2

def init_dict():
    tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    print("tinydict['Name']: ", tinydict['Name'])
    print("tinydict['Age']: ", tinydict['Age'])

    tinydict["AA"] = "aa"
    print(tinydict)


if __name__ == '__main__':
    init_dict()
