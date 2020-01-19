import re


class StrayLetterFlagger:
    """ Flag up lines that contain only a single letter.

    Example:
        "[...]and wi his faird brekkis doun bews about.

        T

        Furth o that steid I went, [...]"

    will flag up the 'T'.

    NOTE: This is a workaround for an issue apparently caused by PDFMiner.
    Without apparent reason a letter will be stripped of a word and placed
    somewhere else in the document.
    """

    name = 'StrayLetterFlagger'
    desc = 'Flag up lines containing only a single letter'

    def __call__(self, text: str):
        lines = text.splitlines()

        for i in range(len(lines)):
            match = self.find_stray_letter(lines[i])
            if match:
                print('Stray letter found, line {}: {}'.format((i+1), lines[i]))

    @staticmethod
    def find_stray_letter(line: str):
        """ Return match object for stray letter in line.

        A stray letter is a letter that appears on a line entirely on its own.

        Args:
            line (str): Line to be searched.

        Returns:
            Match object: Match object if a letter is found on a line on its own,
            None otherwise
        """
        res = None
        if len(line) == 1:                          # We're not interested for
            res = re.search(r'\b[A-Za-z]\b', line)  # matches within a longer line.
        return res
