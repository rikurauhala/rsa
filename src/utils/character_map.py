from utils.dictionary import CHARACTERS


class CharacterMap:
    """Turns characters into integers and integers into characters.
    
    Implements a custom data structure to map characters to order numbers
    and vice versa. See the documentation for a list of supported characters.
    """

    def __init__(self):
        """Initializes a new CharacterMap."""
        self._CHARACTERS = CHARACTERS
        self._ORDER = {chr: ord for ord, chr in CHARACTERS.items()}

    def get_chr(self, ord):
        """Turns a character into an integer.

        Args:
            ord (integer): An integer with a value between 10 and 99.

        Returns:
            chr (character): A character.
        """
        chr = self._CHARACTERS[ord]
        return chr

    def get_ord(self, chr):
        """Turns an integer into a character.

        Args:
            chr (character): A character.

        Returns:
            ord (integer): An integer with a value between 10 and 99.
        """
        ord = self._ORDER[chr]
        return ord
