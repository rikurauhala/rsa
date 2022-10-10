CHARACTERS = {
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f',
    16: 'g',
    17: 'h',
    18: 'i',
    19: 'j',
    20: 'k',
    21: 'l',
    22: 'm',
    23: 'n',
    24: 'o',
    25: 'p',
    26: 'q',
    27: 'r',
    28: 's',
    29: 't',
    30: 'u',
    31: 'v',
    32: 'w',
    33: 'x',
    34: 'y',
    35: 'z',
    36: 'å',
    37: 'ä',
    38: 'ö',
    39: 'A',
    40: 'B',
    41: 'C',
    42: 'D',
    43: 'E',
    44: 'F',
    45: 'G',
    46: 'H',
    47: 'I',
    48: 'J',
    49: 'K',
    50: 'L',
    51: 'M',
    52: 'N',
    53: 'O',
    54: 'P',
    55: 'Q',
    56: 'R',
    57: 'S',
    58: 'T',
    59: 'U',
    60: 'V',
    61: 'W',
    62: 'X',
    63: 'Y',
    64: 'Z',
    65: 'Å',
    66: 'Ä',
    67: 'Ö',
    68: '0',
    69: '1',
    70: '2',
    71: '3',
    72: '4',
    73: '5',
    74: '6',
    75: '7',
    76: '8',
    77: '9',
    78: ' ',
    79: '!',
    80: '"',
    81: '%',
    82: '&',
    83: '(',
    84: ')',
    85: '*',
    86: '+',
    87: ',',
    88: '-',
    89: '.',
    90: '/',
    91: ':',
    92: ';',
    93: '<',
    94: '=',
    95: '>',
    96: '?',
    97: '@',
    98: '_',
    99: '€'
}

ORDER = {chr: ord for ord, chr in CHARACTERS.items()}

class CharacterMap:
    """Turns characters into integers and integers into characters.
    
    Implements a custom data structure to map characters to order numbers
    and vice versa. See the documentation for a list of supported characters.
    """

    def __init__(self):
        """Initializes a new CharacterMap."""

    def get_chr(self, ord):
        """Turns a character into an integer.

        Args:
            ord (integer): An integer with a value between 10 and 99.

        Returns:
            chr (character): A character.
        """
        chr = CHARACTERS[ord]
        return chr

    def get_ord(self, chr):
        """Turns an integer into a character.

        Args:
            chr (character): A character.

        Returns:
            ord (integer): An integer with a value between 10 and 99.
        """
        ord = ORDER[chr]
        return ord
