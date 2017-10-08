class Rule:
    def __init__(self,premisses,conclusions,id,state=False):
        self.premisses=premisses
        self.conclusions=conclusions
        self.id=id
        self.state=state

    def isSelectable(self,facts):
        for premisse in self.premisses:
            if(premisse not in facts):
                return False
        return True


