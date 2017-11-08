from unittest import TestCase
from expression import Expression
from unification import *


class TestUnifier(TestCase):


    def displayFunction(self,ch):
        s=str(ch).split(',')
        #print(s)
        i=0
        for c in s:
            if '[' in c:
                print(c.split('[')[1].replace('\'',''),'(',end='')
                i=i+1
            elif ']' in c:
                print(c.split(']')[0].replace('\'',''), end='')
                for i in range(0,i):
                    print(')',end='')
            else:
                print(c.replace('\'',''),',',end='')

    def mgu(self,exp1,exp2):

        d=unifier(exp1,exp2)
        # print(d)
        # if d is None:
        #     print(d,'\n')
        #     return
        #
        # for key, value in d.items():
        #
        #     if ']' in str(value):
        #         print('(',key,'/ ',end='')
        #         self.displayFunction(str(value))
        #         print(')',end='')
        #
        #     else:
        #         print('(', key, '/', value, ')', end='')
        # if(d==None):
        #     print(None)
        #     print("Unification impossible!")
        #     print("Unification impossible!",file=open("trace.txt","a"))

        print('\n')


    def test_unifier(self):
        ex = Expression("P(?x, f(g(?x)), a)")
        ex2 = Expression('?x')
        print(unifier(ex,ex2))
        #self.mgu(ex,ex2)

    def test_unifier1(self):
        ex = Expression("p(B,C,?x,?z,f(A,?z,B))")
        ex2 = Expression("p(?y,?z,?y,C,?w)")
        print(unifier(ex,ex2))
        # self.mgu(ex,ex2)


    def test_unifier2(self):
        ex = Expression("P(?x, f(g(?x)), a)")
        ex2 = Expression("P(b,?xy, ?z)")
        print(unifier(ex,ex2))
        # self.mgu(ex,ex2)

    def test_unifier3(self):
        ex = Expression("q(f(A,?x),?x)")
        ex2 = Expression("q(f(?z,f(?z,D)),?z)")
        print(unifier(ex,ex2))
        # self.mgu(ex,ex2)

    # def test_unifier3_1(self):
    #     ex = Expression("q(f(A,?x),?x)")
    #     ex2 = Expression("q(f(?z,f(?z,D)),?y)")
    #     #print(unifier(ex,ex2))
    #     self.mgu(ex,ex2)

    def test_unifier4(self):
        ex = Expression("?x")
        ex2 = Expression("g(?x)")
        print(unifier(ex,ex2))
        # self.mgu(ex,ex2)

    def test_unifier5(self):
        ex = Expression("g(f(k(?x)))")
        ex2 = Expression("?N")
        print(unifier(ex,ex2))
        # self.mgu(ex,ex2)

    def test_unifier6(self):
        ex = Expression("?x")
        ex2 = Expression("f(g(?y,a,f(b)))")
        print(unifier(ex,ex2))
        # self.mgu(ex,ex2)

    def test_unifier7(self):
        ex = Expression("f(?r,?d)")
        ex2 = Expression("f(?z)")
        print(unifier(ex,ex2))
        # self.mgu(ex,ex2)




class Fun:
    def __init__(self,name,args:list):
        self.name=name
        self.args=args
