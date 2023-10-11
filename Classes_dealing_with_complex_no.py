import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        number = Complex(real, imaginary)
        return(number)
        
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        number = Complex(real, imaginary)
        return (number)
        
    def __mul__(self, no):
        real = self.real* no.real - self.imaginary*no.imaginary
        imaginary = self.imaginary*no.real + no.imaginary*self.real
        number = Complex(real, imaginary)
        return (number)
        
    def __truediv__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        
        real = ((a*c + b*d)/(c**2 + d**2))
        imaginary = ((b*c - a*d)/(c**2 + d**2))
        number = Complex(real, imaginary)
        return number

    def mod(self):
        c = (self.real**2 + self.imaginary**2)**(1/2)
        r = ( Complex(c, 0))
        if r != None:
            return(r)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')