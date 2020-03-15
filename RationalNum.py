


class RationalNumber():

    def lcm(a, b):
    '''calculate the least common multiple of two positive integers'''
    #print(' in lcm ')
    return (a*b)//gcd(a,b)

    def gcd(bigger, smaller):
        '''compute the greatest common divisor of two positive integers'''
    #print(' in gcd ')
    if not bigger > smaller :
        bigger, smaller = smaller, bigger
    while smaller != 0:
        remainder = bigger % smaller
        
        bigger, smaller = smaller, remainder
    return bigger 

    def __init__(self,Numerator= 0,Denominator= 1):
        if type(Numerator)!= int and type(Denominator)!= int :
            raise(ValueError("Numerator and Denominator should be integers"))
        self.Numerator = Numerator
        self.Denominator = Denominator

    def getDenominator(self):
        return self.Denominator 

    def getNumerator(self):
        self.Numerator

    def toString(self):
        if self.Denominator == 1:
            return str(self.numer)  
        
        else:
           return str(self.numer)  + '/'  +  str(self.denom)
    
    def add( self, rnum):
        '''Add two Rationals'''

        if type(rnum) == RationalNumber:
            # find the lcm
            the_lcm = lcm(self.Denominator, rnum.Denominator)
            # multiply each numerator by the lcm, then add
            numerator_sum = the_lcm*self.Numerator/self.Denominator + \
                        the_lcm*rnum.Numerator/rnum.Denominator
            return RationalNumber( int(numerator_sum), the_lcm )
        else:
            print("Wrong type in addition method.")
            raise(ValueError)
        
        
    
    def subtract( self, rnum):
        if
        the_lcm = lcm(self.denom, param_Rational.denom)
        # multiply each numerator by the lcm, then add
        numerator_sum = the_lcm*self.numer/self.denom - \
                    the_lcm*param_Rational.numer/param_Rational.denom
        return Rational( int(numerator_sum), the_lcm )

    def multiply( self, rnum):
       '''multiply two Rationals'''
        if type(rnum) == RationalNumber:
            # multiply  numerator
            numerator_mul = self.Numerator * rnum.Numerator
            # multiply denominator
            denominator_mul = self.Denominator * rnum.Denominator
            return RationalNumber( int( numerator_mul), int(denominator_mul))
        else:
            print("Wrong type in multiplication method.")
            raise(ValueError)
    def divide( self, rnum):
        '''divide two Rationals'''
        if type(rnum) == RationalNumber:
            # multiply  numerator
            numerator_mul = self.Numerator * rnum.Denominator
            # multiply denominator
            denominator_mul = self.Denominator * rnum.Numerator
            return RationalNumber( int( numerator_mul), int(denominator_mul))
        else:
            print("Wrong type in division method.")
            raise(ValueError)

