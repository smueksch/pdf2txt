import re


class FootnoteFlagger:
    """ Flag up potential footnotes. """

    #TODO: this has a lot of false positives up to the point where it takes
    #      longer using this flagger than without. It also doesn't seem to
    #      catch all actual footnotes, so there are false negatives too.

    name = 'FootnoteFlagger'
    desc = 'Flag up potential footnotes'

    def __call__(self, raw_text: str):
        lines = raw_text.splitlines()

        for i in range(len(lines)):
            if self.is_footnote(lines[i]):
                print('Potential footnote, line {i}: <{f}>'.format(i=i+1,
                                                                   f=lines[i]))

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
        return re.match(r' ?(\w| )+:', line)
