import unittest

from guess import Guess

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('def ault')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('i')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('qp')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

    def testGuess(self):
        self.assertFalse(self.g1.guess('a'))
        self.assertTrue(self.g1.guess('t'))
        self.assertTrue(self.g1.guess('u'))
        self.assertTrue(self.g1.guess('d'))
        self.assertTrue(self.g1.guess('f'))
        self.assertTrue(self.g1.guess('i'))
        self.assertFalse(self.g1.guess('qp'))
        self.assertFalse(self.g1.guess('l'))


if __name__ == '__main__':
    unittest.main()
