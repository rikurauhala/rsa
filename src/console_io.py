class ConsoleIO:
    """Console user input/output."""

    def __init__(self):
        pass

    def print(self, string):
        """Prints the given string to the console.

        Args:
            string: String to be printed.
        """
        print(string)

    def read(self):
        """Reads user input.

        Returns:
            user_input: User input read from the console.
        """
        user_input = input("> ")
        return user_input
