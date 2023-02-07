import unittest
from brickbreaker_main import *

class BrickbreakerTest(unittest.TestCase):

    def test_amounts():
        assert len(walls) == 4, "incorrect amount of walls"

    def test_types():
        assert type(all_blocks) == list, "incorrect type"