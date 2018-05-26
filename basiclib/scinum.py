#과학적 계산을 하기 위한 숫자 체계(목표만 거창해)
#정수의 무한 표현/소수의 무한 표현/연산 이후 수의 표현에 따른 오차 발생이 없는 숫자를 목표로 해서 개발


class SciNum:
    #수의 정수 영역
    class Integer:
        pass

    #수의 소수 영역
    class Decimal:
        pass

    #수의 복소수 영역
    class Complex:
        pass

    #소수에 대한 유효 숫자를 정해주는 메소드
    def set_significant_figure(self,figure):
        pass

    #사칙 연산에 대한 정의
    def __add__(self, other):
        pass