'''
2016-08-11 Version 0.2
Made by indosm
'''
import math
DEBUG = 1
class Var:
    def __init__(self,data=None):
        self.data = data
        self.count = math.floor(math.log2(len(self.data)))
    def run(self):
        self.split()
    def split(self):
        self.cell=[[]for _ in range(self.count)]
        for i in range(len(self.data)):
            self.cell[i//math.ceil(len(self.data)/self.count)].append(self.data[i])
        del self.data
        if DEBUG:
            print(self)
    def __repr__(self):
        return str(self.cell)
