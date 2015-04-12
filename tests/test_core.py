import unittest
from symbolic.core import (MatrixType, argument_sender, CallableObject,
    ExpressionString, BinaryRelation, EqualOperator)


class TestMatrixType(unittest.TestCase):
    def test_MatrixType_vector(self):
        v = MatrixType([0, 0, 0])
        self.assertEqual(v._array, [0, 0, 0])

    def test_MatrixType_vector_interface(self):
        """Should define a 3-vector of numbers"""
        u = MatrixType**3;
        self.assertEqual(u._array, MatrixType([0, 0, 0])._array)

    def test_MatrixType_matrix(self):
        A = MatrixType([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(A._array, array)

    def test_MatrixType_matrix_interface(self):
        A = MatrixType**3*3
        array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(A._array, array)

    def test_MatrixType_matrix_getitem(self):
        A = MatrixType([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        item = A[1][2]
        self.assertEqual(item, 6)

    def test_three_dimensions_MatrixType_matrix_interface(self):
        A = MatrixType**3*3*2
        array = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ]
        self.assertEqual(A._array, array)


class FunctionTest(unittest.TestCase):
    def test_argument_sender(self):
        """The coroutine object created with argument_sender should
        yield the value sended and return the value again in the next
        iteration."""
        sender = argument_sender()
        next(sender)
        a = sender.send(2)
        b = next(sender)
        self.assertEqual(a, 2)
        self.assertEqual(b, 2)

    def test_CallableObject(self):
        double = CallableObject(x*2 for x in MatrixType)
        self.assertEqual(8, next(double(4)))

    def test_many_variables(self):
        add = MatrixType(x + y for x, y in MatrixType)
        added = add(3, 4)
        self.assertEqual(7, next(added))

    def test_CallableObject_string(self):
        """Should make a correct code if use some CallableObject object."""
        double = MatrixType(x*2 for x in MatrixType)
        expr = MatrixType(double(y) for y in MatrixType)
        self.assertEqual(expr.expression, 'double(y)')

    def test_CallableObject_string_with_many_variables(self):
        """Should make a correct code if use some CallableObject object."""
        add = MatrixType(x + y for (x, y) in MatrixType)
        expr = MatrixType(add(x, y) + add(1, 2) for (x, y) in MatrixType)
        self.assertEqual(expr.expression, 'add(x, y)+(add(1, 2))')

    def test_eval_method(self):
        cube = MatrixType(x**3 for x in MatrixType)
        self.assertEqual(27, cube.eval(3))

    def test_eval_method_with_many_variables(self):
        pow = MatrixType(x**y for (x, y) in MatrixType)
        self.assertEqual(27, pow.eval(3, 3))


class ExpressionTest(unittest.TestCase):
    def test_bynary_left_operators(self):
        add = MatrixType(x+2 for x in MatrixType)
        and_ = MatrixType(x&2 for x in MatrixType)
        div = MatrixType(x/2 for x in MatrixType)
        eq = MatrixType(x==2 for x in MatrixType)
        floordiv = MatrixType(x//2 for x in MatrixType)
        ge = MatrixType(x>=2 for x in MatrixType)
        gt = MatrixType(x>2 for x in MatrixType)
        le = MatrixType(x<=2 for x in MatrixType)
        lshift = MatrixType(x<<2 for x in MatrixType)
        lt = MatrixType(x<2 for x in MatrixType)
        matmul = MatrixType(x@2 for x in MatrixType)
        mod = MatrixType(x%2 for x in MatrixType)
        mul = MatrixType(x*2 for x in MatrixType)
        ne = MatrixType(x!=2 for x in MatrixType)
        or_ = MatrixType(x|2 for x in MatrixType)
        pow = MatrixType(x**2 for x in MatrixType)
        rshift = MatrixType(x>>2 for x in MatrixType)
        sub = MatrixType(x-2 for x in MatrixType)
        truediv = MatrixType(x/2 for x in MatrixType)
        xor = MatrixType(x^2 for x in MatrixType)

        self.assertEqual(add.expression, 'x+(2)')
        self.assertEqual(and_.expression, 'x&(2)')
        self.assertEqual(div.expression, 'x/(2)')
        self.assertEqual(eq.expression, 'x==(2)')
        self.assertEqual(floordiv.expression, 'x//(2)')
        self.assertEqual(ge.expression, 'x>=(2)')
        self.assertEqual(gt.expression, 'x>(2)')
        self.assertEqual(le.expression, 'x<=(2)')
        self.assertEqual(lshift.expression, 'x<<(2)')
        self.assertEqual(lt.expression, 'x<(2)')
        self.assertEqual(matmul.expression, 'x@(2)')
        self.assertEqual(mod.expression, 'x%(2)')
        self.assertEqual(mul.expression, 'x*(2)')
        self.assertEqual(ne.expression, 'x!=(2)')
        self.assertEqual(or_.expression, 'x|(2)')
        self.assertEqual(pow.expression, 'x**(2)')
        self.assertEqual(rshift.expression, 'x>>(2)')
        self.assertEqual(sub.expression, 'x-(2)')
        self.assertEqual(truediv.expression, 'x/(2)')
        self.assertEqual(xor.expression, 'x^(2)')

    def test_bynary_right_operators(self):
        radd = MatrixType(2+x for x in MatrixType)
        rand = MatrixType(2&x for x in MatrixType)
        rdiv = MatrixType(2/x for x in MatrixType)
        rfloordiv = MatrixType(2//x for x in MatrixType)
        rlshift = MatrixType(2<<x for x in MatrixType)
        rmatmul = MatrixType(2@x for x in MatrixType)
        rmod = MatrixType(2%x for x in MatrixType)
        rmul = MatrixType(2*x for x in MatrixType)
        ror_ = MatrixType(2|x for x in MatrixType)
        rpow = MatrixType(2**x for x in MatrixType)
        rrshift = MatrixType(2>>x for x in MatrixType)
        rsub = MatrixType(2-x for x in MatrixType)
        rtruediv = MatrixType(2/x for x in MatrixType)
        rxor = MatrixType(2^x for x in MatrixType)

        self.assertEqual(radd.expression, '(2)+x')
        self.assertEqual(rand.expression, '(2)&x')
        self.assertEqual(rdiv.expression, '(2)/x')
        self.assertEqual(rfloordiv.expression, '(2)//x')
        self.assertEqual(rlshift.expression, '(2)<<x')
        self.assertEqual(rmatmul.expression, '(2)@x')
        self.assertEqual(rmod.expression, '(2)%x')
        self.assertEqual(rmul.expression, '(2)*x')
        self.assertEqual(ror_.expression, '(2)|x')
        self.assertEqual(rpow.expression, '(2)**x')
        self.assertEqual(rrshift.expression, '(2)>>x')
        self.assertEqual(rsub.expression, '(2)-x')
        self.assertEqual(rtruediv.expression, '(2)/x')
        self.assertEqual(rxor.expression, '(2)^x')

    def test_unary_operators(self):
        invert = MatrixType(~x for x in MatrixType)
        neg = MatrixType(-x for x in MatrixType)
        pos = MatrixType(+x for x in MatrixType)

        self.assertEqual(invert.expression, '~(x)')
        self.assertEqual(neg.expression, '-(x)')
        self.assertEqual(pos.expression, '+(x)')

    def test__name__property(self):
        """The MatrixType() instance shoud have the __name__ property."""
        named_lambda = MatrixType(+x for x in MatrixType)
        self.assertEqual(named_lambda.__name__, 'named_lambda')


class TestBinaryRelation(unittest.TestCase):
    def setUp(self):
        self.ineq = BinaryRelation('x', '<', 5)

    def test_basic_properties(self):
        self.assertEqual(self.ineq.left, 'x')
        self.assertEqual(self.ineq.operator, '<')
        self.assertEqual(self.ineq.right, 5)

    def test__repr__(self):
        obtained = repr(self.ineq)
        expected = 'BinaryRelation(x < 5)'
        self.assertEqual(expected, obtained)

    def test__eq__(self):
        first = BinaryRelation('x', '>=', 1)
        second = BinaryRelation('x', '>=', 1)
        self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()
