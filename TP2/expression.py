class Expression(list):

    def __init__(self,expr):
        self.expression=expr

    def isAtom(self):
        return (len(self.expression)==1)

    def isVariable(self):
        return self.isAtom() and self.expression[0].find('?')!="-1"

    def separate(self):
        first = [self.expression[0]]
        queue=list(self.expression[1:])
        return first,queue

    def substitute(self,sub:dict):





    def __contains__(self,expr2):
        #epr3 = expr2.split(()[1].split(])[0]
        return self.expression in expr2.split(',')

    #expr = a,b,c,d