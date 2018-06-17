#coding:utf-8
import classicphysics.mechanics.measurement as meas
import math

'''
일차원 운동계에서의 물리식
별 쓸모 없어 보일 수도 있으나(실제로도 별 쓸모 없기는 하다) 결국 2차원계 운동도 3차원계 운동이라는 것도 1차원계 운동계를를 2개 3개
겹쳐 두고서 이것을 서술해 준것에 불과하다고 볼수도 있다.

중요한 것은 힘을 구성하는 성분을 분리해서 단순화 시키는 것을 생각해낸 분이 대단하단 것이지(갈릴레오 선생님?)
'''

#2장 1차원운동(Mothin in One dimension)

class Position_1D(meas.Length):
    #생성자 (첫 위치 0.0, 단위 'm')
    def __init__(self,x_f= meas.Length(0.0,'m')):
        self.position_x= x_f       #x축(1차원계)상에서의 위치 객체 생성

    #포지션의 값 메소드
    def get_position(self):
        return self.position_x.get_length()
    #포지션의 단위 값 메소드
    def get_unit(self):
        return self.position_x.get_unit()

    def set_position(self,x_f):
        self.position_x=x_f

    def set_unit(self,unit):
        self.unit=unit

class Velocity_1D(meas.Standard):
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

#1차원에서의 등가속도 운동

#시간의 함수로 나타낸 속도
def v_f(v_xi : Velocity_1D, a_x : Velocity_1D, time : meas.Time ):
    try:
        v_f = v_xi.get() + a_x.get()*time.get()
    except meas.UnitException:
        pass
    return v_f

#속도와 시간의 함수로 나타낸 위치
def x_f(x_i , v_xi, v_xf, t):
    x_f = x_i.get() + 1/2*(v_xi.get()+v_xf)*t
    return x_f

#시간의 함수로 나타낸 위치
def x_f(x_i, v_xi, a_x, t):
    """

    :rtype: object
    :param x_i: 
    :param v_xi: 
    :param a_x: 
    :param t: 
    :return: 
    """
    x_f = x_i + v_xi*t+1/2*a_x*math.pow(t,2)
    return x_f

#위치의 함수로 나타낸 속도
def v_xf(v_xi,a_x,x_f,x_i)
    v_xf = math.sqrt(math.pow(v_xi,2)+2*a_x*(x_f-x_i))
    return v_xf
