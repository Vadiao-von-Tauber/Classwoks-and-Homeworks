import unittest

from parametrized import parametrized

from CalcEngine import CalcEngine


data = [[18, 10, 8], [2, 10, -8], [-18, -10, -8]]


class CalcEngineTest (unittest.TestCase):
    def setUp(self):
        self.calc_engine = CalcEngine()


    def tearDown(self):
        del self.calc_engine


    def test_upper(self):
        # 1A
        input_string = 'foo'
        expected_result = 'FOO'
        # 2A
        result = input_string.upper()
        # 3A
        self.assertEqual(result, expected_result)


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestCalcEngine:
        def test_add(self):
            for _expected_result, _a, _b in data:
            a = _a
            b = _b
            expected_result = _expected_result
            result = self.calc_engine.add(a, b)
            self.assertEqual(result, expected_result)


        @parametrized.expand([
            [12, 20, 0]
            [28, 20, -8]
            [-12, -10, -8],
        ])

        def test_sub(self, _expected_result, _a, _b):
        #    calc_engine = CalcEngine()
            a = _a
            b = _b
            expected_result = _expected_result
            result = self.calc_engine.sub(a, b)
            self.assert_Equal(result, expected_result)


        def test_mul(self):
        #    calc_engine = CalcEngine()
            a = 12
            b = 10
            expected_result = 120
            result = self.calc_engine.mul(a, b)
            self.assert_Equal(result, expected_result)


        def test_div(self):
        #    calc_engine = CalcEngine()
            a = 100
            b = 10
            expected_result = 10
            result = self.calc_engine.div(a, b)
            self.assert_Equal(result, expected_result)


 #       def test_div_by_zero(self):
 #           calc_engine = CalcEngine()
 #           a = 100
 #           b = 0
 #           # SystemExit
 #           with pytest.raises(ZeroDivisionError):
 #               result = calc_engine.div(a, b)
