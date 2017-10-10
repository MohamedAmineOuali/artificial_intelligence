from fait import Fait
from rule import Rule

color_schema='\x1b[%sm %s \x1b[0m'


# ToDO change the id of regle to a key on a map
class BaseRegle:

    def __init__(self,filename):
        self.filename=filename
        self.rules = []

        with open(filename, 'r') as file:
            for line in file:
                # delete any unecessary white space
                line = ' '.join(line.lower().split())
                rule_number = line.split(":")[0].split("r")[1]
                line = line.split(":")[1]
                line = line.split("si ")[1].split(" alors ")
                premisses = line[0].split(" et ")
                conclusions = line[1].split(" et ")
                self.rules.append(Rule(premisses, conclusions, rule_number))

        self.rules.sort(key=lambda x: int(x.id))

    def print_regles(self):
        print(color_schema%('4;94;15',"voici la liste des regles: "))
        with open(self.filename) as file:
            for line in file:
                print(' '.join(line.replace('\n', "").split()))


class BaseFait:

    def __init__(self,filename):
        self.filename=filename

        # each line in the BF_file is a BF
        self.factsBase= []
        with open(filename, 'r') as file:
            for line in file:
                facts=[]
                line = ' '.join(line.split()).replace(' ', '').split(":")[1]
                columns = line.split(',')
                for fact in columns:
                    facts.append(Fait(fact))
                self.factsBase.append(facts)

    def __contains__(self,myfact):
        return myfact in self.facts

    def choose_BF_from_BFs(self,number):
        self.facts=self.factsBase[number]

    def print_faits(self):
        print("voici la liste des faits: ",self.facts)

    def print_all(self):
        print(color_schema%('4;94;15',"voici les base des faits trouvées"))
        for i,facts in enumerate(self.factsBase):
            print(i+1,": ",facts)