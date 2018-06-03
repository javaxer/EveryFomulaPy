#vector 클래스에 대한 테스트 파일
import unittest
import classicphysics.mechanics.vectors as ve


class Vector_Test(unittest.TestCase):

    def test_get_definition(self):

        v1 = ve.CoordinateSystem(1,1)
        #v1.get_coordinate()

    '''def test_Length(self):
        len1 = measurement.Length()
        len1.set(10.0)
        self.assertEqual(10.0,len1.get(),"결과정상")

    def test_Length(self):
        len2 = measurement.Length(0.0)
        len2.get_definition()
        len2.set(10.0)
        print(len2.get(), 'm')

    def test_compare(self):
        len1 = measurement.Length(10.0,'m')
        ma1 = measurement.Mass(10.0,'kg')
        self.assertFalse(measurement.compare_unit(len1,ma1))'''

if __name__=='__main__':
    unittest.main()