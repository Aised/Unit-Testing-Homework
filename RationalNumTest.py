import  unittest
from RationalNum import RationalNumber

class RationalNumTest(unittest.TestCase):

    def test_zeroAsDenomTest(self):
        self.Rat = RationalNumber(1,0)
        self.assertRaises(ValueError("Denominator can't be 0"),self.Rat )

    def test_defaultRationalNumber(self):
        self.Rat = RationalNumber()
        self.assertEqual(0,self.Rat.getNumerator())
        self.assertEqual(1,self.Rat.getDenominator())
        
    def test_denomTest(self):
        self.Rat = RationalNumber(1, 2)
        self.assertEqual(2,self.Rat.getDenominator(),"Denominator isn't being retrieved correctly")

    def test_numTest(self):
        Rat = RationalNumber(-1, 3)
        self.assertEqual(-1,Rat.getNumerator(),"Numerator isn't being retrieved correctly")

    def test_bothNegativeTest(self):
        Rat = RationalNumber(-1,-3)
        self.assertEqual(1,Rat.getNumerator())
        self.assertEqual(3,Rat.getDenominator())

    def test_rationalTest(self):
        Rat = RationalNumber(5,4)
        self.assertTrue(isinstance(Rat.getNumerator(), int))
        self.assertTrue(isinstance(Rat.getDenominator(), int))

    # normal numbers without reduction / zero num or denom
    def testSubtractingTest(self):

        r = RationalNumber(1, 3)
        s = RationalNumber(7, 3)
        result = r.subtract(s)

        self.assertEquals(-6, result.getNumurator(), "numbers not subtracted correctly")
        self.assertEquals(3, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingTestWithZeroDenom(self):

        r = RationalNumber(1, 0)
        s = RationalNumber(7, 0)
        result = r.subtract(s)

        self.assertRaises(ValueError("denominator can't be 0"), r)
        self.assertRaises(ValueError("denominator can't be 0"), s)

    def testSubtractingTestWithZeroNumur(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(0, 3)
        result = r.subtract(s)

        self.assertEquals(0, result.getNumurator(), "numbers not subtracted correctly")
        self.assertEquals(1, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingTestWithOneZeroNum(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(7, 3)
        result = r.subtract(s)

        self.assertEquals(-7, result.getNumurator(), "numbers not subtracted correctly")
        self.assertEquals(3, result.getDenominator(), "numbers not subtracted correctly")
    
    def testSubtractingTestWithOneZeroDenom(self):

        r = RationalNumber(5, 0)
        s = RationalNumber(7, 3)
        result = r.subtract(s)

        self.assertRaises(ValueError("denominator can't be 0"), r) 

    
    def testSubtractingTestWithOneNegative(self):

        r = RationalNumber(-2, 3)
        s = RationalNumber(7, 3)
        result = r.subtract(s)

        self.assertEquals(-9, result.getNumurator(), "numbers not subtracted correctly")
        self.assertEquals(3, result.getDenominator(), "numbers not subtracted correctly")
    
    def testSubtractingTestWithZero(self):

        r = RationalNumber(-2, 3)
        s = RationalNumber(0, 3)
        result = r.subtract(s)

        self.assertEquals(-2, result.getNumurator(), "numbers not subtracted correctly")
        self.assertEquals(3, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingTestWithTwoNegatives(self):

        r = RationalNumber(-1, 3)
        s = RationalNumber(-7, 3)
        result = r.subtract(s)

        self.assertEquals(6, result.getNumurator(), "numbers not subtracted correctly")
        self.assertEquals(3, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingTestWithTwoNegatives2(self):

        r = RationalNumber(1, -3)
        s = RationalNumber(7, -3)
        result = r.subtract(s)

        self.assertEquals(-6, result.getNumurator(), "numbers not subtracted correctly")
        self.assertEquals(3, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingTestWithOneNegative2(self):

        r = RationalNumber(2, 3)
        s = RationalNumber(-7, 3)
        result = r.subtract(s)

        self.assertEquals(9, result.getNumurator(), "numbers not subtracted correctly")
        self.assertEquals(3, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingTestWithTwoNegativeZeros(self):

        r = RationalNumber(-0, 3)
        s = RationalNumber(-0, 3)
        result = r.subtract(s)

        self.assertEquals(0, result.getNumurator(), "numbers not subtracted correctly")
        self.assertEquals(1, result.getDenominator(), "numbers not subtracted correctly")

    

        

if __name__ == '__main__':
    unittest.main()