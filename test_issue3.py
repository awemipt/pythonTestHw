import unittest
from issue3 import fit_transform

class TestCountLetters(unittest.TestCase):
    def test_1(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = fit_transform([
            'Russia', 'USA', 'United kingdom',
            'Denmark', 'Germany', 'China', 'USA'
        ])
        expected = [
            ('Russia', [0, 0, 0, 0, 0, 1]),
            ('USA', [0, 0, 0, 0, 1, 0]),
            ('United kingdom', [0, 0, 0, 1, 0, 0]),
            ('Denmark', [0, 0, 1, 0, 0, 0]),
            ('Germany', [0, 1, 0, 0, 0, 0]),
            ('China', [1, 0, 0, 0, 0, 0]),
            ('USA', [0, 0, 0, 0, 1, 0])
        ]
        self.assertEqual(actual, expected)

    def test_3(self):
        actual = fit_transform([
            'Russia', 'USA', 'United kingdom',
            'Denmark', 'Germany', 'China', 'USA'
        ])
        expected = ('USA', [0, 0, 0, 0, 0, 1])
        self.assertNotIn(expected, actual)

    def test_4(self):
        actual = fit_transform(
            'Russia', 'USA', 'United kingdom',
            'Denmark', 'Germany', 'China', 'USA'
        )
        expected = [
            ('Russia', [0, 0, 0, 0, 0, 1]),
            ('USA', [0, 0, 0, 0, 1, 0]),
            ('United kingdom', [0, 0, 0, 1, 0, 0]),
            ('Denmark', [0, 0, 1, 0, 0, 0]),
            ('Germany', [0, 1, 0, 0, 0, 0]),
            ('China', [1, 0, 0, 0, 0, 0]),
            ('USA', [0, 0, 0, 0, 1, 0])
        ]
        self.assertEqual(actual, expected)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()
