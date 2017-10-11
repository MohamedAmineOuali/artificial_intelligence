def first_rule(rules,facts):
    for rule in rules:
        if(not(rule.state) and rule.isSelectable(facts)):
            return rule
    return None



def rule_with_more_premisses(rules,faits):
    select=None
    for rule in rules:
        if(not(rule.state) and rule.isSelectable(faits)):
            if(select==None or len(select.premisses)<len(rule.premisses)):
                select=rule
    return select