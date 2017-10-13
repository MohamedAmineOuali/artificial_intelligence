from fait import Fait
from bases import BaseFait,BaseRegle
color_schema='\x1b[%sm %s \x1b[0m'

def chainage_avant(BR:BaseRegle,BF:BaseFait,conflict,goal):

    activated_rules_order=[(None,list(BF.facts))]

    if (goal!='' and goal in BF):
        return BF,activated_rules_order

    #in non goal in BF
    if(Fait.non_fait(goal) in BF):
        print('goal n\'est pas démontrable car on a non but' )
        return BF,activated_rules_order

    rule = conflict(BR.rules, BF.facts)


    while (rule != None):
        # declare that you activated the rule
        rule.state = True


        # test if the goal exists through the conclusions of that rule
        for conclusion in rule.conclusions:
            if (conclusion not in BF):
                BF.facts.append(Fait(conclusion, rule.id))

                # in non goal in BF
                if (Fait.non_fait(conclusion) in BF):
                    print('erreur fait et non fait dans la meme base')
                    return None, activated_rules_order

            else:
                a=0

        # trace
        activated_rules_order.append((rule.id, list(BF.facts)))

        if goal!='' and goal in BF:
            return BF,activated_rules_order

         # in non goal in BF
        if (Fait.non_fait(goal) in BF):
             print('goal n\'est pas démontrable car on a non but')
             return None, activated_rules_order

        # search for the next rule to activate
        rule = conflict(BR.rules, BF.facts)

    return BF,activated_rules_order

# ToDO create la fonction de traçage
def trace(BR:BaseRegle,activated_rules_order,file):
    rules={rule.id:rule for rule in BR.rules}
    for it in activated_rules_order:
        if(it[0]==None):
            print(color_schema%('8;92;1' ,"base de fait initial :"),it[1],file=file)
        else:
            print(color_schema%('1;94;95' ,"la regle declenchée est :"), rules[it[0]],file=file)
            print(color_schema%('8;92;1' ,"la nouvelle base de fait :"),it[1],file=file)