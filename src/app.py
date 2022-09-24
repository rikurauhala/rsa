from functions.crypt import Crypt
from functions.keygen import KeyGenerator

from console_io import ConsoleIO

COMMANDS = {
    "q": "q - quit",
    "h": "h - print the command list",
    "1": "1 - generate keys",
    "2": "2 - encrypt message",
    "3": "3 - decrypt message"
}


class Application:
    """The main application logic."""

    def __init__(self):
        self._io = ConsoleIO()
        self._key_generator = KeyGenerator()
        self._crypt = Crypt()

    def start(self):
        """Starts the main application loop."""

        self._io.print("Application\n")
        self._print_commands()
        self._keys = {}

        c = -1
        m = 12345

        while True:
            command = self._io.read().lower()
            match command:
                case "q":
                    break
                case "h":
                    self._print_commands()
                case "1":
                    self._keys = self._key_generator.generate_keys()
                case "2":
                    # message to be read from input and converted to integer
                    c = self._crypt.encrypt(m, self._keys["e"], self._keys["n"])
                    self._io.print(f"Encrypted message: {c}")
                case "3":
                    # message to be read from input and converted to integer
                    m = self._crypt.decrypt(c, self._keys["d"], self._keys["n"])
                    self._io.print(f"Decrypted message: {m}")
                case _:
                    self._io.print("Invalid command!")

    def _print_commands(self):
        self._io.print("Commands:")
        for command in COMMANDS.items():
            self._io.print(command[1])
