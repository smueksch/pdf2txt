import re


class NumberFlagger:
    """ Flag up lines that contain numbers.

    Use this to point out any lines that potentially have left-over footnote
    numbers in them but in a way they cannot be removed automatically.
    """

    name = 'NumberFlagger'
    desc = 'Flag up lines that contain numbers'

    def __call__(self, text: str):
        lines = text.splitlines()

        for i in range(len(lines)):
            match = self.find_number(lines[i])
            if match:
                context = self.get_context(match.start(), match.end(), lines[i])
                print('Number found, line {}: {}'.format((i+1), context))

    @staticmethod
    def find_number(line: str):
        """ Return match object for number in line.

        Args:
            line (str): Line to be searched.

        Returns:
            Match object: Match object if a number is found, None otherwise.
        """
        return re.search(r'([0-9]+)', line)

    @staticmethod
    def get_context(start: int, end: int, line: str, radius: int = 8) -> str:
        """ Return context for given term in line.

        The context of a term is the immediately surrounding characters. The
        number of characters is given by the radius.

        Take for example the sentence:

            "Sore was I ere I saw Eros."

        with the term starting at 11 and ending at 14, i.e. "ere". Given a
        radius of 8 the context would hence be:

            ">e was I ere I saw e<"

        If there aren't enough characters to the left/right or both then the
        maximum number of characters smaller than the radius is taken instead.

        Args:
            start (int): Index of start of term within line.
            end (int): Index of end of term within line.
            line (str): Line to get context from.
            radius (int, optional): Number of characters left and right of the
                term that should be included as context, defaults to 8.
        Return:
            str: Context of term, including term itself.
        """
        context_start = max(0, start - radius)
        context_end = min(len(line) - 1, end + radius)

        return '<' + line[context_start:context_end] + '>'
