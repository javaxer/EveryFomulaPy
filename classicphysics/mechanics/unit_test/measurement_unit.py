import unittest
import classicphysics.mechanics.measurement as measurement


class Measurement_Standard_Test(unittest.TestCase):

    def test_get_definition(self):
        s1 = measurement.Standard()
        s1.get_definition()

    def test_Length(self):
        len1 = measurement.Length()
        len1.set(10.0)
        self.assertEqual(10.0,len1.get(),"결과정상")

    def test_mass(self):
        ma1 = measurement.Mass(0.0,'kg')
        ma1.get_definition()
        ma1.set(10.0)
        self.assertEqual(10.0,ma1.get(),"결과정상")

    def test_compare(self):
        len1 = measurement.Length(10.0,'m')
        ma1 = measurement.Mass(10.0,'kg')
        self.assertFalse(measurement.compare_unit(len1,ma1))

    def 한글테스트(self):
        길이1 = measurement.길이(10,'m')
        길이1.정의()
        질량1 = measurement.질량(10,'kg')
        질량1.정의()

if __name__=='__main__':
    unittest.main()



mass1 = measurement.Mass(0.0)
mass1.get_definition()
mass1.set(10.0)
print(mass1.get(),'kg')

vol1 = measurement.Volume()
print(vol1.get())
vol1.get_square_volume(len1)
