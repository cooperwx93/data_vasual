from random import choice

class RandomWalk:
    '''生成随机漫步的类'''

    def __init__(self,number=5000):
        self.number = number

        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        '''计算随机漫步包含的所有点'''

        # 不断漫步直到到达指定的次数
        while len(self.x_value) < self.number:
            x_direction = choice([1,-1])
            x_distence = choice(range(5))
            x_step = x_distence * x_direction

            y_direction = choice([1,-1])
            y_distense = choice(range(5))
            y_step = y_distense * y_direction

            if x_step ==0 and y_step==0:
                continue

            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)

