#coding:utf-8

#일차원 운동계에서의 물리식

class Position_1D:
    x_f,x_i,time = 0.0

    def displacement(self,x_f,x_i):
        return self.x_f - x_i

    def average_velociy(self,time):
        return self.displacement(x_f,x_i)/self.time