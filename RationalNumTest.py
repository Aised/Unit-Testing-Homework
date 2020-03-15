import unittest
from RationalNum import RationalNumber

class RationalNum(unittest.TestCase):

    def testzeroAsDenom(self):
         with self.assertRaises(ValueError): RationalNumber(1,0)

    def testdefaultRationalNumber(self):
        self.Rat = RationalNumber()
        self.assertEqual(0,self.Rat.getNumerator())
        self.assertEqual(1,self.Rat.getDenominator())
        
    def testdenom(self):
        self.Rat = RationalNumber(1, 2)
        self.assertEqual(2,self.Rat.getDenominator(),"Denominator isn't being retrieved correctly")

    def testnum(self):
        Rat = RationalNumber(-1, 3)
        self.assertEqual(-1,Rat.getNumerator(),"Numerator isn't being retrieved correctly")

    def testbothNegative(self):
        Rat = RationalNumber(-1,-3)
        self.assertEqual(1,Rat.getNumerator())
        self.assertEqual(3,Rat.getDenominator())

    def testrational(self):
        Rat = RationalNumber(5,4)
        self.assertTrue(isinstance(Rat.getNumerator(), int))
        self.assertTrue(isinstance(Rat.getDenominator(), int))

    def testSimplification(self):
        Rat = RationalNumber(232,2)
        self.assertEqual(116,Rat.getNumerator())
        self.assertEqual(1,Rat.getDenominator())

    def testFullSimplification(self):
        Rat = RationalNumber(112121212121,112121212121)
        self.assertEqual(1,Rat.getNumerator())
        self.assertEqual(1,Rat.getDenominator())

    def testDenomNegative(self):
        Rat = RationalNumber(1,-3)
        self.assertEqual(-1,Rat.getNumerator())
        self.assertEqual(3,Rat.getDenominator())
    
    def testStringRepPositive(self):
        Rat = RationalNumber(1,3)
        self.assertEqual("1/3", str(Rat))
    
    def testStringRepNegative(self):
        Rat = RationalNumber(1,-3)
        self.assertEqual("-1/3", str(Rat))
    
    def testStringRepDenomOne(self):
        Rat = RationalNumber(20,1)
        self.assertEqual("20", str(Rat))
    #Adding
    def testadding(self):

        r = RationalNumber(1, 3)
        s = RationalNumber(7, 3)
        result = r.add(s)

        self.assertEqual(8, result.getNumerator(), "numbers not added correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not added correctly")

    def testaddingWithZeroNumer(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(0, 3)
        result = r.add(s)

        self.assertEqual(0, result.getNumerator(), "numbers not added correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not added correctly")

    def testaddingWithOneZeroNum(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(7, 3)
        result = r.add(s)

        self.assertEqual(7, result.getNumerator(), "numbers not added correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not added correctly")

    def testaddingWithOneNegative(self):

        r = RationalNumber(-2, 3)
        s = RationalNumber(7, 3)
        result = r.add(s)

        self.assertEqual(5, result.getNumerator(), "numbers not added correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not added correctly")

    def testaddingWithTwoNegatives(self):

        r = RationalNumber(-1, 3)
        s = RationalNumber(-7, 3)
        result = r.add(s)

        self.assertEqual(-8, result.getNumerator(), "numbers not added correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not added correctly")

    def testaddingWithTwoNegatives2(self):

        r = RationalNumber(1, -3)
        s = RationalNumber(7, -3)
        result = r.add(s)

        self.assertEqual(-8, result.getNumerator(), "numbers not added correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not added correctly")

    def testaddingWithOneNegative2(self):

        r = RationalNumber(2, 3)
        s = RationalNumber(-7, 3)
        result = r.add(s)

        self.assertEqual(-5, result.getNumerator(), "numbers not added correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not added correctly")

    def testaddingWithTwoNegativeZeros(self):

        r = RationalNumber(-0, 3)
        s = RationalNumber(-0, 3)
        result = r.add(s)

        self.assertEqual(0, result.getNumerator(), "numbers not added correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not added correctly")
    #Subtraction
    def testSubtracting(self):

        r = RationalNumber(1, 3)
        s = RationalNumber(7, 3)
        result = r.subtract(s)

        self.assertEqual(-2, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not subtracted correctly")


    def testSubtractingWithZeroNumer(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(0, 3)
        result = r.subtract(s)

        self.assertEqual(0, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingWithOneZeroNum(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(7, 3)
        result = r.subtract(s)

        self.assertEqual(-7, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not subtracted correctly")
    
    def testSubtractingWithOneNegative(self):

        r = RationalNumber(-2, 3)
        s = RationalNumber(7, 3)
        result = r.subtract(s)

        self.assertEqual(-3, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not subtracted correctly")
    
    def testSubtractingWithOtherZeroNum(self):

        r = RationalNumber(-2, 3)
        s = RationalNumber(0, 3)
        result = r.subtract(s)

        self.assertEqual(-2, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingWithTwoNegatives(self):

        r = RationalNumber(-1, 3)
        s = RationalNumber(-7, 3)
        result = r.subtract(s)

        self.assertEqual(2, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingWithTwoNegatives2(self):

        r = RationalNumber(1, -3)
        s = RationalNumber(7, -3)
        result = r.subtract(s)

        self.assertEqual(2, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not subtracted correctly")
    
    def testSubtractingWithTwoNegatives3(self):

        r = RationalNumber(1, -3)
        s = RationalNumber(-7, 3)
        result = r.subtract(s)

        self.assertEqual(2, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingWithOneNegative2(self):

        r = RationalNumber(2, 3)
        s = RationalNumber(-7, 3)
        result = r.subtract(s)

        self.assertEqual(3, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not subtracted correctly")

    def testSubtractingWithTwoNegativeZeros(self):

        r = RationalNumber(-0, 3)
        s = RationalNumber(-0, 3)
        result = r.subtract(s)

        self.assertEqual(0, result.getNumerator(), "numbers not subtracted correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not subtracted correctly")

    #Multiplication
    def testmultiplicationNoReduction(self):

        r = RationalNumber(4, 3)
        s = RationalNumber(7, 3)
        result = r.multiply(s)

        self.assertEqual(28, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(9, result.getDenominator(), "numbers not multiplied correctly")

    
    def testmultiplicationReductionNotIden(self):

        r = RationalNumber(202, 3)
        s = RationalNumber(3, 4)
        result = r.multiply(s)

        self.assertEqual(101, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(2, result.getDenominator(), "numbers not multiplied correctly")

    def testmultiplicationReductionIden(self):

        r = RationalNumber(22, 3)
        s = RationalNumber(22, 4)
        result = r.multiply(s)

        self.assertEqual(121, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not multiplied correctly")

    def testmultiplicationFullReduction(self):

        r = RationalNumber(22, 22)
        s = RationalNumber(22, 22)
        result = r.multiply(s)

        self.assertEqual(1, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not multiplied correctly")
    
    def testmultiplicationOneReduction(self):

        r = RationalNumber(12121, 1222)
        s = RationalNumber(22, 22)
        result = r.multiply(s)

        self.assertEqual(12121, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(1222, result.getDenominator(), "numbers not multiplied correctly")
    
    def testmultiplicationOtherReduction(self):

        r = RationalNumber(22, 22)
        s = RationalNumber(12121, 1222)
        result = r.multiply(s)

        self.assertEqual(12121, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(1222, result.getDenominator(), "numbers not multiplied correctly")


    def testmultiplicationWithZeroNumer(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(0, 3)
        result = r.multiply(s)

        self.assertEqual(0, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not multiplied correctly")

    def testmultiplicationWithOneZeroNum(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(7, 3)
        result = r.multiply(s)

        self.assertEqual(0, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not multiplied correctly")

    def testmultiplicationWithOneNegative(self):

        r = RationalNumber(-2, 3)
        s = RationalNumber(7, 3)
        result = r.multiply(s)

        self.assertEqual(-14, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(9, result.getDenominator(), "numbers not multiplied correctly")

    def testmultiplicationWithTwoNegatives(self):

        r = RationalNumber(-1, 3)
        s = RationalNumber(-7, 3)
        result = r.multiply(s)

        self.assertEqual(7, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(9, result.getDenominator(), "numbers not multiplied correctly")

    def testmultiplicationWithTwoNegatives2(self):

        r = RationalNumber(1, -3)
        s = RationalNumber(7, -3)
        result = r.multiply(s)

        self.assertEqual(7, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(9, result.getDenominator(), "numbers not multiplied correctly")

    def testmultiplicationWithOneNegative2(self):

        r = RationalNumber(2, 3)
        s = RationalNumber(-7, 3)
        result = r.multiply(s)

        self.assertEqual(-14, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(9, result.getDenominator(), "numbers not multiplied correctly")

    def testmultiplicationWithTwoNegativeZeros(self):

        r = RationalNumber(-0, 3)
        s = RationalNumber(-0, 3)
        result = r.multiply(s)

        self.assertEqual(0, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not multiplied correctly")

    def testmultiplicationWithLessThanOne(self):

        r = RationalNumber(1, 3)
        s = RationalNumber(22, 4)
        result = r.multiply(s)

        self.assertEqual(11, result.getNumerator(), "numbers not multiplied correctly")
        self.assertEqual(6, result.getDenominator(), "numbers not multiplied correctly")
    #Division
    def testDivisionNoReduction(self):

        r = RationalNumber(4, 3)
        s = RationalNumber(7, 3)
        result = r.divide(s)

        self.assertEqual(4, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(7, result.getDenominator(), "numbers not divided correctly")

    
    def testDivisionReductionNotIden(self):

        r = RationalNumber(202, 3)
        s = RationalNumber(3, 4)
        result = r.divide(s)

        self.assertEqual(808, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(9, result.getDenominator(), "numbers not divided correctly")

    def testDivisionReductionIden(self):

        r = RationalNumber(22, 3)
        s = RationalNumber(22, 4)
        result = r.divide(s)

        self.assertEqual(4, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(3, result.getDenominator(), "numbers not divided correctly")

    def testDivisionFullReduction(self):

        r = RationalNumber(22, 22)
        s = RationalNumber(22, 22)
        result = r.divide(s)

        self.assertEqual(1, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not divided correctly")
    
    def testDivisionOneReduction(self):

        r = RationalNumber(12121, 1222)
        s = RationalNumber(22, 22)
        result = r.divide(s)

        self.assertEqual(12121, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(1222, result.getDenominator(), "numbers not divided correctly")
    
    def testDivisionOtherReduction(self):

        r = RationalNumber(22, 22)
        s = RationalNumber(12121, 1222)
        result = r.divide(s)

        self.assertEqual(1222, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(12121, result.getDenominator(), "numbers not divided correctly")


    def testDivisionWithZeroNumer(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(0, 3)
        with self.assertRaises(ZeroDivisionError): r.divide(s)

        

    def testDivisionWithOneZeroNum(self):

        r = RationalNumber(0, 5)
        s = RationalNumber(7, 3)
        result = r.divide(s)

        self.assertEqual(0, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(1, result.getDenominator(), "numbers not divided correctly")

    def testDivisionWithOneNegative(self):

        r = RationalNumber(-2, 3)
        s = RationalNumber(7, 3)
        result = r.divide(s)

        self.assertEqual(-2, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(7, result.getDenominator(), "numbers not divided correctly")

    def testDivisionWithTwoNegatives(self):

        r = RationalNumber(-1, 3)
        s = RationalNumber(-7, 3)
        result = r.divide(s)

        self.assertEqual(1, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(7, result.getDenominator(), "numbers not divided correctly")

    def testDivisionWithTwoNegatives2(self):

        r = RationalNumber(1, -3)
        s = RationalNumber(7, -3)
        result = r.divide(s)

        self.assertEqual(1, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(7, result.getDenominator(), "numbers not divided correctly")

    def testDivisionWithOneNegative2(self):

        r = RationalNumber(2, 3)
        s = RationalNumber(-7, 3)
        result = r.divide(s)

        self.assertEqual(-2, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(7, result.getDenominator(), "numbers not divided correctly")

    def testDivisionWithTwoNegativeZeros(self):

        r = RationalNumber(-0, 3)
        s = RationalNumber(-0, 3)
        with self.assertRaises(ZeroDivisionError): r.divide(s)


    def testDivisionWithLessThanOne(self):

        r = RationalNumber(1, 3)
        s = RationalNumber(22, 4)
        result = r.divide(s)

        self.assertEqual(2, result.getNumerator(), "numbers not divided correctly")
        self.assertEqual(33, result.getDenominator(), "numbers not divided correctly")
    

        

if __name__ == '__main__':
    unittest.main()