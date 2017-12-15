from unification import *
from unification import *


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
        # print(d)
        if d is None or len(d)==0:
            print('\x1b[6;31;20m'+"Unification impossible!"+'\x1b[0m', '\n')
            return

        for key, value in d:

            if ']' in str(value):
                print('(', key, '/ ', end='')
                self.displayFunction(str(value))
                print(')', end='')

            else:
                print('(', key, '/', value, ')', end='')

        print('\n')
        return d








expr1=input('\x1b[26;36;20m' + 'Type the first expression : ' + '\x1b[0m')
expr2=input('\x1b[26;34;20m' + "Type the second expression : " + '\x1b[0m')

e1=Expression(expr1)
e2=Expression(expr2)

result=Display().mgu(e1,e2)


f = open("traeUnification.log",'w')
f.write(str(result))