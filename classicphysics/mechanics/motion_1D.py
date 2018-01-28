#coding:utf-8
import measurement

#일차원 운동계에서의 물리식

#위치
class Position_1D:
    def __init__(self,x_f=0.0,x_i=0.0,time = 0.0,unit='m'):
        self.x_f=measurement.Length(x_f)        #첫번째 위치
        self.x_i=measurement.Length(x_i)        #차후 위치
        self.time = measurement.Time(time)  #시간
        self.unit=unit      #단위(기본은 메타(m)

    def set_displacement_1D(self,x_f,x_i):
        self.x_f = x_f
        self.x_i = x_i

    def get_displacement_1D(self,x_f,x_i):
        self.x_f=x_f
        self.x_i=x_i
        return x_f - x_i

    def get_unit(self):
        return self.unit

    def set_unit(self,unit):
        self.unit=unit

    def get_time(self):
        return time
    def

    def get_average_velociy_1D(self):
        return self.displacement_1D(x_f,x_i)/self.time

    def get_average_speed_1D(self,time):
        return self.get_displacement_1D()


#등가속도 운동
class ConstantAcceleration_1D:


import unittest