import unittest

from app.business.service.memory_game.MemoryGame import MemoryGame


class Test(unittest.TestCase):

    def test_is_list_equal(self):
        mem_game = MemoryGame()
        self.assertEqual(True, mem_game.is_list_equal([1, 2], [2, 1]))

    def test_is_list_is_not_equal(self):
        mem_game = MemoryGame()
        self.assertEqual(False, mem_game.is_list_equal([2, 2], [2, 1]))


if __name__ == '__main__':
    unittest.main()
