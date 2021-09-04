from unittest import TestCase


class Test(TestCase):
    def test_random_odd_integer(self):
        from primgen import random_odd_integer
        self.assertTrue(random_odd_integer(64) % 2 == 1)

    def test_miller_rabin_method(self):
        from primgen import miller_rabin_method
        self.assertTrue(miller_rabin_method(632485520306600051477731141302573178632491, .1) is True)
        self.assertTrue(miller_rabin_method(989086760284979193666271685572629563840964, .01) is False)
