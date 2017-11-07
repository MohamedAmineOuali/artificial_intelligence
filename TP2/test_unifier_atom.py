from unittest import TestCase
from expression import Expression
from unification import *

# class TestUnifier_atom(TestCase):
#     def test_unifier_atom(self):
#         list1 = ['P', '?x', ['f', ['g', '?x']], 'a']
#         ex = Expression(list1)
#         list2 = ['?x']
#         ex2 = Expression(list2)
#
#         x=unifier_atom(ex,ex2)
#         self.assertEqual(x,None)
#
#
#     def test_unifier_atom2(self):
#         list1 = ['P', '?x', ['f', ['g', '?x']], 'a']
#         ex = Expression(list1)
#         list2 = ['?y']
#         ex2 = Expression(list2)
#
#         x=unifier_atom(ex2,ex)
#         self.assertNotEqual(x,None)
#
#     def test_unifier_atom2(self):
#         list1 = ['y']
#         ex = Expression(list1)
#         list2 = ['?y']
#         ex2 = Expression(list2)
#
#         x=unifier_atom(ex2,ex)
#         self.assertNotEqual(x,None)
#
#     def test_unifier_atom2(self):
#         list1 = ['y']
#         ex = Expression(list1)
#         list2 = ['y']
#         ex2 = Expression(list2)
#
#         x=unifier_atom(ex2,ex)
#         self.assertNotEqual(x,None)
#
