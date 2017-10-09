import sys
from bases import BaseFait,BaseRegle
from chainage_avant import chainage_avant,trace

def choix_base():
    BC_number = input('Choisir la base de connaissances 1 ou 2 : ')

    BR = BaseRegle('BC'+BC_number+'/regles.txt')
    BF = BaseFait('BC'+BC_number+'/faits.txt')

    BF.print_all()

    BF_number = int(input('Choisir la base des faits : ')) - 1
    BF.choose_BF_from_BFs(BF_number)

    return (BR,BF)

def choix_conflict_rule():
    choixR=int(input('Choisir le mode de raisonnement :\n'
                 '1 : sélection de la première règle\n'
                 '2 : sélection de la règle ayant le plus de prémisses \n'
                 'Tapez le num correspondant : '))
    #choose the method to use to select the rule
    if choixR==1:
        from conflict_rules import first_rule
        conflict=first_rule
    else:
        from  conflict_rules import rule_with_more_premisses
        conflict=rule_with_more_premisses
    return conflict



BR,BF=choix_base()

BR.print_regles()


conflict=choix_conflict_rule()

goal=input('Choisir le but à chercher(appuyer entrer pour sauter cette étape) : ')

BF,activated_rules_order=chainage_avant(BR,BF,conflict,goal)



if goal in BF:
    print("but trouvé")


trace(BR,activated_rules_order,sys.stdout)

save=int(input('voulez vous enregistrer la trace d\'execution:\n'
                 '1 : yes'
                 '2 : no \n'))
if(save==1):
    filename=input("entrer le nom du fichier")
    trace(BR,activated_rules_order, open(filename,'w'))
