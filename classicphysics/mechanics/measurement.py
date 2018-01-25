#coding:utf-8

#길이의 단위와 그 전환에 대한 정의
#내용은 모두 Serway물리 교과서 내용에서 발췌했음
#처음에는 파일명을 Length라고 했으나 곰곰히 생각해 본 결과 정의(Standard)라고 정의하는 쪽이 더 정확할 것으로 보여
# 파일 명을 수정함.

import math

#기준에 대한 원시 클래스
class Standard:
    #생성자 정의(number는 양, unit은 단위)
    def __init__(self, number=0.0, unit=''):
        self.standard = number
        self.unit = unit
#    def __init__(self):
#        self.standard = 0.0
#    def __init__(self,number):
#        self.standard = number


    def get_definition(self):
        print("기준에 대한 원시 클래스")

    #양을 지정하는 메소드
    def set(self,number):
        self.standard=number

    #양을 얻는 메소드
    def get(self):
        return self.standard

    #단위를 얻는 메소드
    def get_unit(self):
        return self.unit

#SI단위계 표준 단위인 미터에 대한 정의
class Length(Standard):
    # 1m에 대한 물리적인 정의
    speed_of_light = 299792458
    def get_definition(self):
        print("1미터(m)는 진공 속에서 빛이 1/299,792,458초 동안 진행한 거리이다.")
    def set_length(self,length):
        self.set(length)
    def get_lenght(self):
        return self.get()
    def get_speed_of_light(self):
        return self.speed_of_light

#아래의 클래스는 위 길이에 대한 클래스의 한글 클래스이다.
class 길이(Length):
    def 정의(self):
        self.get_definition()
    def 설정(self,number):
        self.set(number)
    def 획득(self):
        self.get()


class Mass(Standard):
    #1kg에 대한 물리적인 정의
    def get_definition(self):
        print("1킬로그램(kg)은 프랑스 국제 도량형국에 보관되어 있는 특정한 백금-이리듐합금 실린더로 정의된다.")

#아래의 클래스는 위 질량에 대한 클래스의 한글 클래스이다.
class 질량(Mass):
    def 정의(self):
        self.get_definition()
    def 설정(self,number):
        self.set(number)
    def 획득(self):
        self.get()


class Time(Standard):
    #1sec에 대한 물리적인 정의
    def get_definition(self):
            print("1초(sec)는 세슘 원자로 부터 방축되는 복사 진동주기의 9,1,92,631,770배이다")

#아래의 클래스는 위 시간에 대한 클래스의 한글 클래스이다.
class 길이(Time):
    def 정의(self):
        self.get_definition()
    def 설정(self,number):
        self.set(number)
    def 획득(self):
        self.get()   


class Volume(Standard):
    #부피에 대한 정의, 기초적인 산수 영역이나 아래의 밀도에 대한 정의를 위해 추가한다.

    #정육면체의 부피에 대한 공식
    def get_square_volume(self,length):
        return math.pow(length.get(),3)

    # 직육면체에 부피에 대한 공식
    def get_rectengular_volume(self,length_x, length_y, length_z):
        return length_x*length_y*length_z

class 부피(Volume):
    def 설정(self,number):
        self.set(number)
    def 획득(self,number):
        self.get(number)
    def 직육면체부피(self,length):
        self.get()

class Density:
    def getdensity(self, mass, volume):
        return mass/volume

class 밀도(Density):
    def 획득(self,mass, volume):
        return self.getdensity(mass,volume)

class DimensionalAnalysis:
    #차원 분석에 대한 클래스, 현시점에서는 검증용 외에는 별다른 용도가 없으므로 일단 통과하자
    pass

class ConversionOfUnits:
    #단위 환산에 대한 내용, 일단 이 부분도 패스(SI단위만 사용할 거니까)
    pass