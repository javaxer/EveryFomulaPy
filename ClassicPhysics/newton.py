#coding:utf-8

#이 주로 뉴턴 역학과 관련된 사항을 정리해 둔 파일이다
#사실상 계산식으로 표현된 물리학의 시작이나 마찬가지인 부분이니 나의 작업의 최초 영역으로써 적합하다고 본다

import numpy as np 


#뉴튼 클래스 여기서 부터 모든 것이 시작된느 추상 클래스다.
class Newton():
   g=9.8	#지구의 중력 가속도(9.8m/s^2)

   def __init__(self):
       return
        
   #중력 가속도 반환
   def getgravity(self):
       return self.g

   def help(self):
       print("이것은 뉴튼 함수의 추상 클래스입니다.")


#제 1법칙 관성의 법칙
#Lex Prima : Newotn's First Law of Motion - Inertia
class Inertia(Newton):
    def help(self):
        print("외부에서 가해지는 힘이 없을 때, 물체는 운동상태를 유지한다.")

    def getInertia(self):
        print("외부에서 가해지는 힘이 없을 때, 물체는 운동상태를 유지한다.")

#제 2법칙 가속도의 법칙
#Lex secunda 
class AccelationLaw(Newton):
    def help(self):
        print("외부에서 가해지는 힘은 물체의 운동상태를 변화시킨다.")
