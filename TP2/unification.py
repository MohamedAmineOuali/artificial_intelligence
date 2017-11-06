from expression import Expression


def unifier_atom(expr1:Expression,expr2:Expression):
    if(expr2.isAtom()):
        expr1,expr2=expr2,expr1

    if(expr1==expr2):
        return {}

    if(expr1.isVariable()):#1 seul element + contains "?"
        if(expr1 in expr2):
            return None

        return {expr1,expr2}

def unifier(terms1:Expression,terms2:Expression):

    if(terms1.isAtom() or terms1.isAtom()): #atom is var, cste = 1 seul elt dans liste
        return unifier_atom(terms1,terms2)

    F1,T1=terms1.separate()#return 2 lists : [first elt] [..rest..]
    F2,T2=terms2.separate()


    Z1=unifier(F1,F2)
    if(Z1==None):
        return None

    G1=T1.substitute(Z1)
    G2=T2.substitute(Z1)


    Z2=unifier(G1,G2)

    if(Z2==None):
        return None

    return {Z1,Z2}


