from os import name, system

from functions.crypt import Crypt
from functions.keygen import KeyGenerator

from console_io import ConsoleIO

COMMANDS = {
    "q": "[ q ] quit",
    "h": "[ h ] print the command list",
    "1": "[ 1 ] generate keys",
    "2": "[ 2 ] encrypt message",
    "3": "[ 3 ] decrypt message",
    "4": "[ 4 ] show public key",
    "5": "[ 5 ] show private key"
}


class Application:
    """The main application logic."""

    def __init__(self):
        """Initializes a new instance of the application."""
        self._io = ConsoleIO()
        self._key_generator = KeyGenerator()
        self._crypt = Crypt()
        self._keys = {}
        self._message_m = -1
        self._message_c = -1

    def start(self):
        """Starts the main application loop."""

        self._io.print("Application\n")
        self._print_commands()

        while True:
            command = self._io.read().lower()
            self._clear_console()
            match command:
                case "q":
                    break
                case "h":
                    self._print_commands()
                case "1":
                    self._io.print("Generating keys...")
                    self._keys = self._key_generator.generate_keys()
                    self._io.print("Keys generated!")
                case "2":
                    self._io.print("Enter a message:")
                    self._message_m = self._io.read()
                    self._message_c = self._crypt.encrypt(
                        self._message_m,
                        self._keys["e"],
                        self._keys["n"]
                    )
                    self._io.print(f"Encrypted message: {self._message_c}")
                case "3":
                    self._message_m = self._crypt.decrypt(
                        self._message_c,
                        self._keys["d"],
                        self._keys["n"]
                    )
                    self._io.print(f"Decrypted message: {self._message_m}")
                case "4":
                    self._io.print("Public key")
                    n = self._keys["n"]
                    self._io.print(f"n: {n}")
                    e = self._keys["e"]
                    self._io.print(f"e: {e}")
                case "5":
                    self._io.print("Private key")
                    n = self._keys["n"]
                    self._io.print(f"n: {n}")
                    d = self._keys["d"]
                    self._io.print(f"d: {d}")
                case _:
                    self._io.print("Invalid command!")

    def _print_commands(self):
        """Prints a list of available commands."""
        self._io.print("Commands:")
        for command in COMMANDS.items():
            self._io.print(command[1])

    def _clear_console(self):
        """Clears the console after each command."""
        if name == "nt":
            system("cls")
        else:
            system("clear")
