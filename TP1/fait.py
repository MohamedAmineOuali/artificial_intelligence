
class Fait:
    def __init__(self,fact,rule_number=None):
        self.fact=fact
        self.rule_number=rule_number

    #each line in the BF_file is a BF
    @staticmethod
    def retreive_BFs_form_file(BC_number):
        BFs=[]
        facts=[]
        file_name='BC'+BC_number+'\\faits.txt'
        with open(file_name,'r') as file:
            for line in file:
                line=' '.join(line.split()).replace(' ','').split(":")[1]
                columns=line.split(',')
                for fact in columns:
                    facts.append(Fait(fact))
                BFs.append(facts)
                facts=[]
        return BFs

    #return the desired BF from its number
    @staticmethod
    def choose_BF_from_BFs(BFs):
        BF_number=int(input('Choisir la base des faits : '))-1
        facts=BFs[BF_number]
        return facts
