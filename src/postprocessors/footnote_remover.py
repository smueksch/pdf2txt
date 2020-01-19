import re


class FootnoteRemover:
    """ Remove obvious footnotes. """

    name = 'FootnoteRemover'
    desc = 'Remove obvious footnotes'

    def __call__(self, raw_text: str):
        lines = raw_text.splitlines(True)
        text = ''

        for line in lines:
            #if self.is_footnote(line):
            #    print('Footnote:' + line)
            if not self.is_footnote(line):
                text = text + line

        return text

    @staticmethod
    def is_footnote(line: str) -> bool:  # Tested: Actually only removes the footnote lines.
        """ Return true if line matches footnote pattern.

        Args:
            line (str): Line to be tested.

        Returns:
            bool: True if line matches footnote pattern, false otherwise.
        """
        # Here we explicitly DO want to use 'match' and not 'search', as we need
        # the match to occur at the start of the line.
        return re.match(r'[0-9]+\.\s*', line)
        # OLD: return re.match(r'[0-9]+ {2,3}\w+.*', line)
