import unittest
import measurement


class Measurement_Standard_Test(unittest.TestCase):

    def test_get_definition(self):
        s1 = measurement.Standard()
        s1.get_definition()

    def test_Length(self):
        len1 = measurement.Length()
        len1.set(10.0)
        self.assertEqual(10.0,len1.get(),"결과정상")

    def test_Length(self):
        len2 = measurement.Length(0.0)
        len2.get_definition()
        len2.set(10.0)
        print(len1.get(), 'm')

if __name__=='__main__':
    unittest.main()




길이1 = measurement.길이(0.0)
길이1.정의()

mass1 = measurement.Mass(0.0)
mass1.get_definition()
mass1.set(10.0)
print(mass1.get(),'kg')

vol1 = measurement.Volume()
print(vol1.get())
vol1.get_square_volume(len1)
