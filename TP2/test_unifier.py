from unittest import TestCase
from expression import Expression
from unification import *

class TestUnifier(TestCase):
    def test_unifier(self):
        ex = Expression("P(?x, f(g(?x)), a)")
        ex2 = Expression('?x')
        print(unifier(ex,ex2))

    def test_unifier1(self):
        ex = Expression("p(B,C,?x,?z,f(A,?z,B))")
        ex2 = Expression("p(?y,?z,?y,C,?w)")
        print(unifier(ex,ex2))

    def test_unifier2(self):
        ex = Expression("P(?x, f(g(?x)), a)")
        ex2 = Expression("P(b,?xy, ?z)")
        print(unifier(ex,ex2))

    def test_unifier3(self):
        ex = Expression("q(f(A,?x),?x)")
        ex2 = Expression("q(f(?z,f(?z,D)),?z)")
        print(unifier(ex,ex2))

    def test_unifier3_1(self):
        ex = Expression("q(f(A,?x),?x)")
        ex2 = Expression("q(f(?z,f(?z,D)),?y)")
        print(unifier(ex,ex2))

    def test_unifier4(self):
        ex = Expression("?x")
        ex2 = Expression("g(?y)")
        print(unifier(ex,ex2))