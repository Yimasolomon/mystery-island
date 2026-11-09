
import unittest

from player import (
    create_player,
    use_energy,
    restore_energy,
    add_item,
    has_item
)


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = create_player("Alex")

    def test_create_player(self):
        self.assertEqual(self.player["name"], "Alex")
        self.assertEqual(self.player["energy"], 100)
        self.assertEqual(self.player["inventory"], [])

    def test_use_energy(self):
        result = use_energy(self.player, 20)

        self.assertTrue(result)
        self.assertEqual(self.player["energy"], 80)

    def test_insufficient_energy(self):
        self.player["energy"] = 15

        result = use_energy(self.player, 30)

        self.assertFalse(result)
        self.assertEqual(self.player["energy"], 15)

    def test_restore_energy(self):
        use_energy(self.player, 40)
        restore_energy(self.player, 30)

        self.assertEqual(self.player["energy"], 90)

    def test_energy_cannot_exceed_100(self):
        restore_energy(self.player, 30)

        self.assertEqual(self.player["energy"], 100)

    def test_add_item(self):
        result = add_item(self.player, "compass")

        self.assertTrue(result)
        self.assertIn("compass", self.player["inventory"])

    def test_prevent_duplicate_items(self):
        add_item(self.player, "compass")
        result = add_item(self.player, "compass")

        self.assertFalse(result)
        self.assertEqual(self.player["inventory"].count("compass"), 1)

    def test_has_item(self):
        add_item(self.player, "key")

        self.assertTrue(has_item(self.player, "key"))
        self.assertFalse(has_item(self.player, "treasure"))


if __name__ == "__main__":
    unittest.main()
