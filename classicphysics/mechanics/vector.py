#coding:utf-8

#물리학 교과서 3장에 나오는 백터 역학에 대한 정리
import math

class CoordinateSystem:         #평면 극 좌표계(Plane polar coordinates)(r,theta)


    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_coordinate(self):
        r = math.sqrt(x**2+y**2)
        theta = math.degrees(math.atan2(y,x))


class vector:
    x,y,z=0
    xi,yi,zi=0
    setvector(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        pass
    getvector(self):
        return self
    getx(self):
        return self.x
    gety(self):
        return self.y
    getz(self):
        return self.y
    magnitude(self,vector vector1,vector vector2):
        pass


