a, b, c = map(int, input("Enter a, b, c: ").split(','))
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def geta(self):
        return self.a
    def getb(self):
        return self.b
    def getc(self):
        return self.c
    def getDiscriminant(self):
        return self.b**2-4*self.a*self.c
    def getRoot1(self):
        if ((self.b**2)-4*self.a*self.c)>0:
            eqn = (((-1)*self.b)+((self.b**2-4*self.a*self.c)**(1/2)))/2*self.a
            print('The roots are {}'.format(eqn), end = "")
        elif ((self.b**2)-4*self.a*self.c) == 0 :
            eqn3 =  (((-1)*self.b)+((self.b**2-4*self.a*self.c)**(1/2)))/2*self.a
            print('The root is {}'.format(eqn3))
        else :
            print("The equation has no roots")
    def getRoot2(self):
        if (self.b**2-4*self.a*self.c)>0:
            eqn2 =  (((-1)*self.b)-((self.b**2-4*self.a*self.c)**(1/2)))/2*self.a
            print(" and {}".format(eqn2))
        else :
            pass
def main():
    r = QuadraticEquation(a,b,c)
    return r.getRoot1(), r.getRoot2()
main()
