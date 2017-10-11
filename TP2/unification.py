from expression import *


def unifier_atom(expr1:Expression,expr2:Expression):
    if(expr2.isAtom()):
        expr1,expr2=expr2,expr1

    if(expr1==expr2):
        return {}

    if(expr1.isVariable()):
        if(expr1 in expr2):
            return None
        return

def unifier(expr1:Expression,expr2:Expression):



    if(expr1.isAtom() or expr1.isAtom()):
        return unifier_atom(expr1,expr2)

    F1,T1=expr1.separate()
    F2,T2=expr2.separate()


    Z1=unifier(F1,F2)
    if(Z1==None):
        return None

    G1=T1.substitute(Z1)
    G2=T2.substitute(Z1)


    Z2=unifier(G1,G2)

    if(Z2==None):
        return None

    return Z1,Z2



