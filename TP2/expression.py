import ast
class Expression(list):

    def __init__(self,expr):
        self.expression=expr

    def isAtom(self):
        return (len(self.expression)<=1)

    def isVariable(self):
        return len(self.expression)==1 and '?' in self.expression[0]

    def separate(self):
        if(isinstance(self.expression[0],list)):
            first = self.expression[0]
        else:
            first = [self.expression[0]]
        queue=self.expression[1:]
        return Expression(first),Expression(queue)

    def __contains__(self, expr):
        tmp = self.expression.__str__()
        return (expr.expression[0] in tmp)

    def __eq__(self, expr):
        return  len(self.expression) == 1 and len(expr.expression)==1 and self.expression[0]==expr.expression[0]


    def substitute(self,subs:dict):
        tmp = self.expression.__str__()
        for v, sub in subs.items():
            v = '\"' + v + "\""
            tmp=tmp.replace(v , sub)
        self.expression = ast.literal_eval(tmp)
