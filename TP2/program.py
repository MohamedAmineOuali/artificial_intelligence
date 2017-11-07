from test_unifier import TestUnifier
from unification import *
from expression import Expression

class Display:

    def displayFunction(self, ch):
        s = str(ch).split(',')
        # print(s)
        i = 0
        for c in s:
            if '[' in c:
                print(c.split('[')[1].replace('\'', ''), '(', end='')
                i = i + 1
            elif ']' in c:
                print(c.split(']')[0].replace('\'', ''), end='')
                for i in range(0, i):
                    print(')', end='')
            else:
                print(c.replace('\'', ''), ',', end='')


    def mgu(self, exp1, exp2):
        d = unifier(exp1, exp2)

        if d is None:
            print("Pas d'unificateur pour ces deux expressions!", '\n')
            return

        for key, value in d.items():

            if ']' in str(value):
                print('(', key, '/ ', end='')
                self.displayFunction(str(value))
                print(')', end='')

            else:
                print('(', key, '/', value, ')', end='')

        print('\n')








expr1=input("Type the first expression")
expr2=input("Type the second expression")

e1=Expression(expr1)
e2=Expression(expr2)

Display().mgu(e1,e2)


