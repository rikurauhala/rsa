from console_io import ConsoleIO

COMMANDS = {
    "q": "q - quit",
    "1": "1 - generate keys",
    "2": "2 - encrypt message",
    "3": "3 - decrypt message"
}


class Application:
    def __init__(self):
        self._io = ConsoleIO()

    def start(self):
        self._io.print("Application\n")
        self._print_commands()

        while True:
            command = self._io.read("command: ")

            match command:
                case "q":
                    break
                case "1":
                    self._generate_keys()
                case _:
                    self._io.print("Invalid command!")
                    self._print_commands()

    def _print_commands(self):
        self._io.print("Commands:")
        for command in COMMANDS:
            self._io.print(COMMANDS[command])

    def _generate_keys(self):
        pass
