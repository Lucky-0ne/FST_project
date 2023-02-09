import unittest
from brickbreaker_main import *

class BrickbreakerTest(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.key.set_repeat(100, 100)
        self.screen = pygame.display.set_mode((400, 300))

    def test_keyboard_input(self):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.assertEqual(event.key, pygame.K_LEFT)

    def test_mouse_input(self):
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(100, 100), button=1))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.assertEqual(event.pos, (100, 100))
                self.assertEqual(event.button, 1)

    def test_amounts(self):
        assert len(walls) == 4, "incorrect amount of walls"

    def test_types(self):
        assert type(all_blocks) == list, "incorrect type"

    def test_quit(self):
        pygame.quit()