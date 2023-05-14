def format_string(string, formatter=None):
    """Format a string using the formatter object, which
    is expected to have a format() method that accepts
    a string."""

    class DefaultFormmater:
        """Format a string in title case."""

        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormmater()

    return formatter.format(string)


hello_string = "hello world, how are you?"
print(" input: " + hello_string)
print(" output: " + format_string(hello_string))
