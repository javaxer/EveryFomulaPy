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
    #생성자 (첫 위치 0.0, 단위 'm')
    def __init__(self,x_f=0.0,unit='m'):
        self.position_x=measurement.Length(x_f,unit)        #x축(1차원계)상에서의 위치 객체 생성

    def get_position(self):
        return self.position_x.get_length()

    def get_unit(self):
        return self.position_x.get_unit()

    def set_unit(self,unit):
        self.unit=unit

class Velocity_1D:
    #생성자
    def __init__(self,velocity=0.0,unit="m/s"):
        self.velocity=velocity
        self.unit=unit

    def get_average_velociy_1D(self,timetable):
        self.displacement = sum(timetable.keys())           #총 변위합
        self.sum_time = sum(timetable.values())             #시간의 총합
        self.velocity = self.displacemnet/self.sum_time
        return self.velocity

class Speed_1D:
    #생성자
    def __init__(self,speed=0.0,unit="m/s"):
        self.speed = speed
        self.unit = unit

    def get_average_speed_1D(self,time):
        return self.get_displacement_1D()

#등가속도 운동
class ConstantAcceleration_1D:



import unittest