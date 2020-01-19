import re


class EOLSpaceRemover:
    """ Remove whitespace at the end of a line.

    Example:
        Original:  "This line ends in whitespace. \n"
        Processed: "This line ends in whitespace.\n"
    """

    name = 'EOLSpaceRemover'
    desc = 'Remove whitespace at the end of a line'

    def __call__(self, raw_text: str) -> str:
        return re.sub(r'[\r\t\f\v ]+\n', r'\n', raw_text)
