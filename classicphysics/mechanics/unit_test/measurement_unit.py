import unittest
import classicphysics.mechanics.measurement as measurement


class Measurement_Standard_Test(unittest.TestCase):

    def test_get_definition(self):
        print("원시 객체 생성")
        s1 = measurement.Standard()
        s1.get_definition()
        print("--------------")

    def test_Length(self):
        print("길이 객체 생성")
        len1 = measurement.Length()
        len1.set(10.0)
        self.assertEqual(10.0,len1.get(),"결과정상")
        print("-------------")

    def test_mass(self):
        print("질량 객체 생성")
        ma1 = measurement.Mass(0.0,'kg')
        ma1.get_definition()
        ma1.set(10.0)
        self.assertEqual(10.0,ma1.get(),"결과정상")
        print("-------------")

    def test_compare(self):
        print("단위간 비교")
        len1 = measurement.Length(10.0,'m')
        len2 = measurement.Length(6,'m')
        ma1 = measurement.Mass(10.0,'kg')
        ma2 = measurement.Mass(5,'kg')

        self.assertFalse(measurement.compare_unit(len1,ma1),"len1과 ma1의 단위는 서로 다름")
        print("-------------")

    def 한글테스트(self):
        길이1 = measurement.길이(10,'m')
        길이1.정의()
        질량1 = measurement.질량(10,'kg')
        질량1.정의()

    def test_angle(self):
        angle1 = measurement.Angle()
        angle2 = measurement.Angle(10,'deg')
        #self.assertEqual(0,angle1.get(),"angle1 각도는 0도")
        #self.assertEqual(10,angle2.get(),"angle2의 각도는 10도")

if __name__=='__main__':
    unittest.main()


'''
mass1 = measurement.Mass(0.0)
mass1.get_definition()
mass1.set(10.0)
print(mass1.get(),'kg')

vol1 = measurement.Volume()
print(vol1.get())
vol1.get_square_volume(len1)
'''
