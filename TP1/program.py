from fait import Fait
from rule import Rule

BFs=[]
rules=[]
myBF=[]

BC_number=input('Choisir BC 1 ou 2 : ')
choixR=int(input('Choisir le mode de conflits des règles : '))
goal=input('Choisir le but à chercher : ')

rules=Rule.retrieve_rules_from_file(BC_number)
BFs=Fait.retreive_BFs_form_file(BC_number)
myBF=Fait.choose_BF_from_BFs(BFs)


def first_rule(rules,facts):
    for rule in rules:
        if(not(rule.state) and rule.isSelectable(facts)):
            return rule
    return None

def rule_with_more_premisses(rules,faits):
    select=None
    for rule in rules:
        if(not(rule.etat) and rule.isSelectable(faits)):
            if(select==None or len(select.premisses)<len(rule.premisses)):
                select=rule
    return select

def fact_exists_in_BF(myfact,facts):
    for fact in facts:
        if(fact.fact==myfact):
            return True
    return False

def print_myBF():
    print("voici la liste des faits")
    for fact in myBF:
        print(fact)

#choose the method to use to select the rule
if choixR==1:
    conflict=first_rule
else:
    conflict=rule_with_more_premisses
#stop if the goal is found(goal specified)
if(goal!=""):
    #test if the goal is already in the BF
    if(fact_exists_in_BF(goal,myBF)):
        print('But Trouvé!')
        exit()
    #select the 1st rule to activate
    rule=conflict(rules,myBF)
    while(rule!=None):
        #declare that you activated the rule
        rule.state = True
        #test if the goal exists through the conclusions of that rule
        for conclusion in rule.conclusions:
            if(not fact_exists_in_BF(conclusion,myBF)):
                myBF.append(Fait(conclusion,rule.id))
            if goal==conclusion:
                print('But trouvé!')
                exit()
        #search for the next rule to activate
        rule = conflict(rules, myBF)
    print("but non trouvé")
    exit()
#run through all the deductible BFs
else:
    #select the 1st rule to activate
    rule=conflict(rules,myBF)
    while(rule!=None):
        #declare that you activated the rule
        rule.state = True
        #add the conclusions to the BF
        for conclusion in rule.conclusions:
            myBF.append(Fait(conclusion,rule.id))
        #search for the next rule to activate
        rule = conflict(rules, myBF)
    print("List of BF (acheivable goals):")
    for fact in myBF:
        print(fact.fact)
