import re

# You may wanna try ExcessiveNewlineRemover first, it'll probably give you
# better results.


class DoubleNewlineFixer:
    """ Replace double newlines with a single one. """

    name = 'DoubleNewlineFixer'
    desc = 'Replace double newlines with a single one'

    def __call__(self, raw_text: str):
        return re.sub(r'(\n+)(?=.)', r'\n', raw_text)
