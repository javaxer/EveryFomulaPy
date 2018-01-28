#coding:utf-8
import measurement

'''
일차원 운동계에서의 물리식
별 쓸모 없어 보일 수도 있으나(실제로도 별 쓸모 없기는 하다) 결국 2차원계 운동도 3차원계 운동이라는 것도 1차원계 운동계를를 2개 3개
겹쳐 두고서 이것을 서술해 준것에 불과하다고 볼수도 있다.

중요한 것은 힘을 구성하는 성분을 분리해서 단순화 시키는 것을 생각해낸 분이 대단하단 것이지(갈릴레오 선생님?)
'''

#위치
class Position_1D:
    #생성자 (첫 위치 0.0
    def __init__(self,x=0.0,unit='m'):
        self.x=measurement.Length(x)        #1차원 상의 위치
        self.time = measurement.Time(time)  #시간
        self.unit=unit      #단위(기본은 메타(m)

    #
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
    def set_time(self,time):
        self.time = time

    def get_average_velociy_1D(self):
        return self.displacement_1D(x_f,x_i)/self.time

    def get_average_speed_1D(self,time):
        return self.get_displacement_1D()


#등가속도 운동
class ConstantAcceleration_1D:


import unittest