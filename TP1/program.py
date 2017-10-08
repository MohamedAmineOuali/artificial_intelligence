# coding=utf-8
from fait import Fait
from rule import Rule

faits=[]
rules=[]

choixR=int(input('Choisir le mode de conflits des règles : '))
but=input('Choisir le but à chercher : ')
BR=input('Choisir la base des règles : ')
BF=input('Choisir la base des faits : ')

with open(BF,'r') as f:
    for line in f:
        colonnes=line.split(',')
        for fait in colonnes:
            faits.append(Fait(fait))

with open(BR,'r') as f:
    for i,line in enumerate(f):
        line=line.replace(' ','').replace('\n','')
        colonnes=line.split('alors')
        premisses=colonnes[0].split('et')
        conclusions=colonnes[1].split('et')
        rules.append(Rule(premisses,conclusions,i))



def firstRule(rules,faits):
    for rule in rules:
        if(not(rule.etat) and rule.isSelected(faits)):
            return rule

    return None

def morePre(rules,faits):
    select=None
    for rule in rules:
        if(not(rule.etat) and rule.isSelected(faits)):
            if(select==None or len(select.premisses)<len(rule.premisses)):
                select=rule
    return select


def exist(conc,faits):
    for fait in faits:
        if(fait.fait==conc):
            return True
    return False

if(exist(but,faits)):
    print('But Trouvé!')
    exit()

if choixR==1:
    conflict=firstRule
else:
    conflict=morePre

regle=conflict(rules,faits)
while(regle!=None):
    regle.etat = True
    for conc in regle.conclusions:
        if(not exist(conc,faits)):
            faits.append(Fait(conc,regle.id))
        if but==conc:
            print('But trouvé!')
            exit()
    regle = conflict(rules, faits)

