
class Fait:
    def __init__(self,fact,rule_number=None):
        self.fact=fact
        self.rule_number=rule_number

    def __eq__(self, other):
        return self.fact==other

    def __repr__(self):
        return self.fact