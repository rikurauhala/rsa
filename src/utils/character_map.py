from utils.dictionary import CHARACTERS


class CharacterMap:
    """Turns characters into integers and integers into characters.

    Implements a custom data structure to map characters to order numbers
    and vice versa. See the documentation for a list of supported characters.
    """

    def __init__(self):
        """Initializes a new CharacterMap."""
        self._characters = CHARACTERS
        self._order = {chr: ord for ord, chr in CHARACTERS.items()}

    def get_character(self, order):
        """Turns a character into an integer.

        Args:
            order (integer): An integer with a value between 10 and 99.

        Raises:
            KeyError: If the order number is not mapped to a character.
            TypeError: If the order number is not a valid integer.

        Returns:
            char (character): A character.
        """

        if order < 10 or order > 99:
            raise KeyError("Order number must be between 10 and 99")
        if not isinstance(order, int):
            raise TypeError("Order number must be an integer")
        char = self._characters[order]
        return char

    def get_order(self, char):
        """Turns an integer into a character.

        Args:
            char (character): A character.

        Raises:
            KeyError: If the character is not supported.

        Returns:
            order (integer): An integer with a value between 10 and 99.
        """

        if char not in self._order:
            raise KeyError(f"Character {char} is not supported")
        order = self._order[char]
        return order
