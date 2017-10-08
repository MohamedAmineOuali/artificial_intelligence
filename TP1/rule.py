class Rule:
    def __init__(self,premisses,conclusions,id,etat=False):
        self.premisses=premisses
        self.conclusions=conclusions
        self.id=id
        self.etat=etat

    def isSelected(self,faits):
        for pre in self.premisses:
            found=False
            for fait in faits:
                if(pre==fait.fait):
                    found=True
                    break
            if(found==False):
                return False
        return True