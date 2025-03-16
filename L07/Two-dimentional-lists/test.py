from math import frexp


from random import randint
def twodimentionallist():
    rows = 3
    cols = 4

    def sumlist(list: list[list[int]]):
        sum = 0
        for i in list:
            for j in i:
                sum += j
        return sum