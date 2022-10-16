from os import name, system

from functions.crypt import Crypt
from functions.keygen import KeyGenerator

from utils.commands import COMMANDS

from console_io import ConsoleIO


class Application:
    """The main application logic."""

    def __init__(self):
        """Initializes a new instance of the application."""
        self._commands = COMMANDS
        self._crypt = Crypt()
        self._io = ConsoleIO()
        self._key_generator = KeyGenerator()
        self._keys = {}
        self._message_m = -1
        self._message_c = -1

    def start(self):
        """Starts the main application loop."""

        self._clear_console()
        self._print_title("RSA")
        self._print_commands()

        while True:
            command = self._io.read().lower()

            if command == "q":
                break
            if command == "h":
                self._print_commands()
            elif command == "1":
                self._generate_keys()
            elif command == "2":
                if self._keys_exist():
                    self._encrypt()
            elif command == "3":
                if self._keys_exist():
                    self._decrypt()
            elif command == "4":
                if self._keys_exist():
                    self._print_public_key()
            elif command == "5":
                if self._keys_exist():
                    self._print_private_key()
            else:
                self._print_invalid_command()

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

    def _print_title(self, text):
        """Prints a title.

        Args:
            text (string): Text to be printed.
        """
        self._io.print(text + "\n")

    def _generate_keys(self):
        """Generates keys."""
        self._print_title("Key generation")
        self._io.print("Generating keys...")
        self._keys = self._key_generator.generate_keys()
        self._io.print("Keys generated!")

    def _encrypt(self):
        """Encrypts a message."""
        self._print_title("Message encryption")
        while True:
            try:
                self._io.print("Enter a message:")
                self._message_m = self._io.read()
                self._message_c = self._crypt.encrypt(
                    self._message_m,
                    self._keys["e"],
                    self._keys["n"]
                )
                self._io.print(f"Encrypted message: {self._message_c}")
                break
            except (KeyError, ValueError) as error:
                self._io.print_error(error)

    def _decrypt(self):
        """Decrypts a message."""
        try:
            self._print_title("Message decryption")
            self._message_m = self._crypt.decrypt(
                self._message_c,
                self._keys["d"],
                self._keys["n"]
            )
            self._io.print(f"Decrypted message: {self._message_m}")
        except KeyError as error:
            self._io.print_error(error)

    def _print_public_key(self):
        self._print_title("Public key")
        n = self._keys["n"]
        self._io.print(f"n: {n}")
        e = self._keys["e"]
        self._io.print(f"e: {e}")

    def _print_private_key(self):
        self._print_title("Private key")
        n = self._keys["n"]
        self._io.print(f"n: {n}")
        d = self._keys["d"]
        self._io.print(f"d: {d}")

    def _print_invalid_command(self):
        self._io.print_error("Invalid command!")

    def _keys_exist(self):
        if not self._keys:
            self._io.print_error("Keys have not been generated yet!")
            return False
        return True
