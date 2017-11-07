from unittest import TestCase
from expression import Expression


class TestExpression(TestCase):
    def test___init__(self):
        ex=Expression("p(B,C,?x,?z,f(A,?z,B))")
        print(ex.expression)

    def test___init__2(self):
        ex = Expression("p(?y,?z,?y,C,?w)")
        print(ex.expression)

    def test___init__3(self):
        ex = Expression("P(?x, f(g(?x)), a)")
        print(ex.expression)

    def test___init__4(self):
        ex = Expression("P(b,?xy, ?z)")
        print(ex.expression)

    def test___init__5(self):
        ex = Expression("q(f(A,?x),?x)")
        print(ex.expression)

    def test___init__6(self):
        ex = Expression("q(f(?z,f(?z,D)),?z)")
        print(ex.expression)

    def test___init__7(self):
        ex = Expression("?x")
        print(ex.expression)

    def test___init__8(self):
        ex = Expression("g(?x)")
        print(ex.expression)


# class TestExpression(TestCase):
#     def test_isAtom(self):
#         self.fail()
#
#     def test_isVariable(self):
#         self.fail()
#
#     def test_separate(self):
#         list1 = ['P', '?x', ['f', ['g', '?x']], 'a']
#         ex = Expression(list1)
#         tete, queue = ex.separate()
#         print(tete)
#         print(queue)
#
#     def test_substitute(self):
#         list1 = ['P', '?x', ['f', ['g', '?x']], 'a']
#         ex = Expression(list1)
#         ex.substitute({'?x': 'b'})
#         print(ex.expression)
#
#
# class TestExpression(TestCase):
#     def test___contains__(self):
#         list1 = ['P', '?x', ['f', ['g', '?x']], 'a']
#         ex = Expression(list1)
#         list2 = ['?y']
#         ex2 = Expression(list2)
#
#         self.assertFalse(ex2 in ex)
#
#     def test___contains__yes(self):
#         list1 = ['P', '?x', ['f', ['g', '?x']], 'a']
#         ex = Expression(list1)
#         list2 = ['?x']
#         ex2 = Expression(list2)
#
#         self.assertFalse(ex2 in ex)
#
#
# class TestExpression(TestCase):
#     def test___eq__(self):
#         list1 = ['?x']
#         ex = Expression(list1)
#         list2 = ['?x']
#         ex2 = Expression(list2)
#         self.assertTrue(ex == ex2)
#
#     def test___eq__2(self):
#         list1 = ['?x']
#         ex = Expression(list1)
#         list2 = ['?y']
#         ex2 = Expression(list2)
#         self.assertFalse(ex == ex2)