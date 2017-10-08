from fait import Fait
from bases import BaseFait,BaseRegle


def chainage_avant(BR:BaseRegle,BF:BaseFait,conflict,goal):

    activated_rules_order=[]

    if (goal!='' and goal in BF):
        print('But Trouvé!')
        exit()

    rule = conflict(BR.rules, BF.facts)


    while (rule != None):
        # declare that you activated the rule
        rule.state = True
        # trace
        activated_rules_order.append(rule.id)

        # test if the goal exists through the conclusions of that rule
        for conclusion in rule.conclusions:
            if (conclusion not in BF):
                BF.facts.append(Fait(conclusion, rule.id))
            else:
                a=0
            if goal!='' and goal == conclusion:
                print('But trouvé!')
                exit()

        # search for the next rule to activate
        rule = conflict(BR.rules, BF.facts)


    print("but non trouver")