
import unittest

from player import create_player
from game import explore_location, solve_cave_puzzle


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player = create_player("Alex")

    def test_explore_beach(self):
        result = explore_location(self.player, "beach")

        self.assertIn("compass", result)
        self.assertIn("compass", self.player["inventory"])
        self.assertIn("beach", self.player["visited"])
        self.assertEqual(self.player["energy"], 95)

    def test_cannot_enter_cave_without_key(self):
        result = explore_location(self.player, "cave")

        self.assertIn("key", result)
        self.assertEqual(self.player["energy"], 100)

    def test_cannot_explore_same_location_twice(self):
        explore_location(self.player, "beach")
        result = explore_location(self.player, "beach")

        self.assertIn("already", result)
        self.assertEqual(self.player["energy"], 95)

    def test_cave_puzzle(self):
        explore_location(self.player, "jungle")
        explore_location(self.player, "cave")

        result = solve_cave_puzzle(self.player, "echo")

        self.assertIn("treasure", result)
        self.assertIn("treasure", self.player["inventory"])

    def test_wrong_puzzle_answer(self):
        explore_location(self.player, "jungle")
        explore_location(self.player, "cave")

        result = solve_cave_puzzle(self.player, "wrong answer")

        self.assertIn("incorrect", result)
        self.assertNotIn("treasure", self.player["inventory"])

    def test_cannot_reach_lighthouse_without_items(self):
        result = explore_location(self.player, "lighthouse")

        self.assertIn("compass", result)
        self.assertEqual(self.player["energy"], 100)

    def test_win_the_game(self):
        explore_location(self.player, "beach")
        explore_location(self.player, "jungle")
        explore_location(self.player, "cave")
        solve_cave_puzzle(self.player, "echo")

        result = explore_location(self.player, "lighthouse")

        self.assertIn("You win!", result)


if __name__ == "__main__":
    unittest.main()
