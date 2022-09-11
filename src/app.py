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
    def __init__(self):
        self._io = ConsoleIO()
        self._key_generator = KeyGenerator()

    def start(self):
        self._io.print("Application\n")
        self._print_commands()

        while True:
            command = self._io.read("> ")
            match command:
                case "q":
                    break
                case "h":
                    self._print_commands()
                case "1":
                    self._key_generator.generate_keys()
                case "2":
                    self._io.print("Functionality not implemented yet!")
                case "3":
                    self._io.print("Functionality not implemented yet!")
                case "4":
                    self._io.print("Functionality not implemented yet!")
                case _:
                    self._io.print("Invalid command!")

    def _print_commands(self):
        self._io.print("Commands:")
        for command in COMMANDS:
            self._io.print(COMMANDS[command])
