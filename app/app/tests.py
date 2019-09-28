from django.test import TestCase

from app.calc import add, sub


class ClassTest(TestCase):


    def test_addnum(self):

        '''Test for addition of numbers'''
        self.assertEqual(add(3,4),7)

    def test_subtructnum(self):

        '''Subtract two numbers'''
        self.assertEqual(sub(4,3),1)
