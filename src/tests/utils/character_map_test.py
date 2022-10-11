import unittest

from utils.character_map import CharacterMap
from utils.dictionary import CHARACTERS


class TestCharacterMap(unittest.TestCase):
    def setUp(self):
        self._character_map = CharacterMap()
        self._characters = CHARACTERS

    def test_character_map_works_with_all_characters(self):
        for _, chr in self._characters.items():
            order_number = self._character_map.get_order(chr)
            self.assertEqual(type(order_number), int)

    def test_order_number_out_of_bounds_raises_key_error(self):
        with self.assertRaises(KeyError, msg="Order number must be between 10 and 99"):
            self._character_map.get_character(9)
        with self.assertRaises(KeyError, msg="Order number must be between 10 and 99"):
            self._character_map.get_character(100)

    def test_order_number_string_raises_type_error(self):
        with self.assertRaises(TypeError, msg="Order number must be an integer"):
            self._character_map.get_character("string")

    def test_character_not_in_the_dict_raises_key_error(self):
        with self.assertRaises(KeyError, msg="Character $ is not supported"):
            self._character_map.get_order('$')
