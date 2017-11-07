from unittest import TestCase
from expression import Expression
from unification import *

class TestUnifier(TestCase):
    def test_unifier(self):
        list1 = ['P', '?x', ['f', ['g', '?x']], 'a']
        ex = Expression(list1)
        list2 = ['?x']
        ex2 = Expression(list2)
        print(unifier(ex,ex2))

    def test_unifier1(self):
        list1 = ['P', '?x', ['f', ['g', '?x']], 'a']
        ex = Expression(list1)
        list2 = ['P', 'b','?xy' , '?z']
        ex2 = Expression(list2)
        print(unifier(ex,ex2))
