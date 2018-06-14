#coding:utf-8

import classicphysics.mechanics.measurement as measure

#물리학 교과서 3장에 나오는 백터 역학에 대한 정리
import math

class CoordinateSystem:         #평면 극 좌표계(Plane polar coordinates)(r,theta)

    #극 좌표계계를 생성하는 생성자. 요는 두개의 좌표 요소가 입력되면 이를 생성하는다는 뜻이다.
    def __init__(self,x,y):
        self.x = measure.Length(x)
        self.y = measure.Length(y)
        self.r = math.sqrt(self.x.get() ** 2 + self.y.get() ** 2)
        self.theta = measure.Degree(math.degrees(math.atan2(y, x)), 'deg')

    #좌표계 자체를 반납하는 메소드
    def get_coordinate(self):
        self.coordinate = CoordinateSystem(self.r,self.theta)
        return coordinate

    #좌표계에서 요소를 반납하는 메소드
    def get_r(self):
        return self.r
    def get_theta(self):
        return self.theta

    #극 좌표계를 직접 입력하는 함수
    def set_coordinate(self,r,theta):
        self.r=r
        self.theta = theta

    #좌표계에서 요소를 입력하는 메소드
    def set_r(self,r):
        self.r=r
    def get_theta(self,theta):
        self.theta=theta


#백터에 대한 클래스
class vector:

    def __init__(self,x,y,z):
        self.x = x.get()
        self.y = y.get()
        self.z = z.get()
        self.unit = x.get_unit()

    def set_vector(self,x,y,z):
        self.x = x.get()
        self.y = y.get()
        self.z = z.get()
        self.unit = x.get_unit()

    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getz(self):
        return self.y




