import re


class NumberOnlyLineRemover:
    """ Remove lines that only consist of a single number.

    Lines that only consists of a single number are likely to be either page
    numbers or leftover footnotes.
    """

    name = 'NumberOnlyLineRemover'
    desc = 'Remove lines that only consist of a single number'

    def __call__(self, raw_text: str):
        lines = raw_text.splitlines(True)
        text = ''

        for line in lines:
            #if self.is_number_only(line):
            #    print('Removing line:', line)
            if not self.is_number_only(line):
                text = text + line

        return text

    @staticmethod
    def is_number_only(line: str) -> bool:
        """ Return True if line only consists of a single number.

        Args:
            line (str): Line to be checked.

        Returns:
            bool: True if line only consists of single number, False otherwise.
        """
        return re.match(r'^[0-9]+$', line)
