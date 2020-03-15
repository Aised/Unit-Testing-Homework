from math import gcd

def lcm(a, b):
        return abs(a*b) // int(gcd(a, b))

class RationalNumber():

    def __init__(self, Numerator=0, Denominator=1):
        if type(Numerator) != int and type(Denominator) != int:
            raise ValueError("Numerator and Denominator should be integers")
        if Denominator == 0:
            raise ValueError("Denominator can't be 0")
        
        if Numerator == 0:
            Denominator =1

        (Numerator, Denominator) = (Numerator / gcd(Numerator,Denominator),Denominator / gcd(Numerator,Denominator))
         

        if Numerator < 0 and Denominator < 0:
            Numerator = abs(Numerator)
            Denominator = abs(Denominator)
            
        elif Numerator > 0 and Denominator <0 :
            Denominator = abs(Denominator)
            Numerator = -1 * Numerator
        
        self.Numerator = int(Numerator) 
        self.Denominator = int(Denominator) 

    def getDenominator(self):
        return self.Denominator

    def getNumerator(self):
        return self.Numerator

    def __str__(self):
        if self.Denominator == 1:
            return str(self.Numerator)

        else:
            return str(self.Numerator) + '/' + str(self.Denominator)

    def add(self, other):
        '''Add two Rationals'''

        if type(other) == RationalNumber:
            # find the lcm
            the_lcm = lcm(self.Denominator, other.Denominator)
            # multiply each numerator by the lcm, then add
            numerator_sum = the_lcm*self.Numerator/self.Denominator + \
            the_lcm*other.Numerator/other.Denominator
            return RationalNumber(int(numerator_sum), the_lcm)
        else:
            print("Wrong type in addition method.")
            raise ValueError

    def subtract(self, other):
        '''subtract two Rationals'''
        if type(other) == RationalNumber:
            the_lcm = lcm(self.Denominator, other.Denominator)
            # multiply each numerator by the lcm, then add
            numerator_sum = the_lcm*self.Numerator/self.Denominator - \
            the_lcm*other.Numerator/other.Denominator
            return RationalNumber(int(numerator_sum), the_lcm)

    def multiply(self, other):
        '''multiply two Rationals'''

        if type(other) == RationalNumber:
            # multiply  numerator
            numerator_mul = self.Numerator * other.Numerator
            # multiply denominator
            denominator_mul = self.Denominator * other.Denominator
            return RationalNumber(int(numerator_mul), int(denominator_mul))
        else:
            print("Wrong type in multiplication method.")
            raise ValueError

    def divide(self, other):
        '''divide two Rationals'''

        if type(other) == RationalNumber:
               # multiply  numerator
            if other.Numerator ==0:
                raise ZeroDivisionError("Numerator of divisor can't be 0")
            numerator_mul = self.Numerator * other.Denominator
            # multiply denominator
            denominator_mul = self.Denominator * other.Numerator
            return RationalNumber(int( numerator_mul), int(denominator_mul))
        else:
            print("Wrong type in division method.")
            raise ValueError


