import re


class ExcessiveNewlineRemover:
    """ Remove excessive amount of newlines.

    Two or more newlines in a row are considered excessive newlines.
    """

    name = 'ExcessiveNewlineRemover'
    desc = 'Trim 2 or more newline in a row down to 2'

    def __call__(self, raw_text: str) -> str:
        return re.sub(r'\n{2}(\n|\s)*', r'\n\n', raw_text)
#        lines = raw_text.splitlines(True)
#        text = ''

#        for i in range(len(lines)):
#            try:
#                if self.is_empty(lines[i]) and \
#                   self.is_empty(lines[i+1]):
#                    pass
#                else:
#                    text = text + lines[i]
#            except IndexError:
#                # Ignore because this only happens if we reached end of text.
#                pass

    # TODO: document this.
    @staticmethod
    def is_empty(line: str) -> bool:
        return not line.strip()
