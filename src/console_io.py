from colored import fg, stylize


class ConsoleIO:
    """Console user input/output."""

    def __init__(self):
        """Initializes a new ConsoleIO object."""

    def print(self, string):
        """Prints the given string to the console.

        Args:
            string: String to be printed.
        """
        print(string)

    def print_error(self, message):
        """Prints a red error message to the console.

        Args:
            message: Error message to be printed.
        """
        style = fg("9")
        error_message = stylize(f"Error: {message}", style)
        print(error_message)

    def print_title(self, text):
        """Prints a title.

        Args:
            text (string): Text to be printed.
        """
        print(text + "\n")

    def read(self):
        """Reads user input.

        Returns:
            user_input: User input read from the console.
        """
        style = fg("47")
        user_input = input(stylize("> ", style))
        return user_input
