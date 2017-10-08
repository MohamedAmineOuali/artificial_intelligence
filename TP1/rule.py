class Rule:
    def __init__(self,premisses,conclusions,id,state=False):
        self.premisses=premisses
        self.conclusions=conclusions
        self.id=id
        self.state=state

    def isSelectable(self,facts):
        for premisse in self.premisses:
            found=False
            for fact in facts:
                if(premisse==fact.fact):
                    found=True
                    break
            if(found==False):
                return False
        return True

    @staticmethod
    def retrieve_rules_from_file(BC_number):
        rules=[]
        file_name='BC'+BC_number+'\\regles.txt'
        new_file=open("tmp.txt","w+")
        with open(file_name ,'r') as file:
            for line in file:
                #delete any unecessary white space
                line=' '.join(line.lower().split())
                rule_number=line.split(":")[0].split("r")[1]
                line=line.split(":")[1]
                line=line.split("si ")[1].split(" alors ")
                premisses=line[0].split(" et ")
                conclusions=line[1].split(" et ")
                rules.append(Rule(premisses,conclusions,rule_number))
        rules.sort(key=lambda x: int(x.id))
        return rules

