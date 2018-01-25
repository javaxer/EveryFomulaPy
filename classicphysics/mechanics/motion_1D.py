#coding:utf-8

#일차원 운동계에서의 물리식

#위치
class Position_1D:
    def __init__(self,x_f=0.0,x_i=0.0,time = 0.0):
        self.x_f=x_f        #첫번째 위치
        self.x_i=x_i        #차후 위치
        self.time=time      #시간

    def displacement_1D(self,x_f,x_i):
        self.x_f=x_f
        self.x_i=x_i
        return x_f - x_i

    def average_velociy_1D(self,time):
        return self.displacement_1D(x_f,x_i)/self.time

    def average_speed_1D(self,distance,time):
        return

#속도
class Velocity_1D:
    pass

class Speed_1D:
    pass

class Accelaeration:
    pass

#등가속도 운동
class ConstantAcceleration_1D:
