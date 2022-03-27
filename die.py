from random import randint

class Die:
    '''表示一个骰子的类'''

    def __init__(self, num_sizes=6):
        '''骰子默认6面'''
        self.num_sizes = num_sizes

    def roll(self):
        '''返回一个随机数'''
        return randint(1, self.num_sizes)
