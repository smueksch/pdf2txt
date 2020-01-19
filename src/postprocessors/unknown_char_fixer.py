import re


class UnknownCharFixer:
    """ Replace unknown character with best interpretation. """

    name = 'UnknownCharFixer'
    desc = 'Replace unknown character with best interpretation'

    def __call__(self, raw_text: str):
        text = re.sub(u'', r'0', raw_text)
        text = re.sub(u'', r'1', text)
        text = re.sub(u'', r'2', text)
        text = re.sub(u'', r'3', text)
        text = re.sub(u'', r'4', text)
        text = re.sub(u'', r'5', text)
        text = re.sub(u'', r'6', text)
        text = re.sub(u'', r'7', text)
        text = re.sub(u'', r'8', text)
        return re.sub(u'', r'9', text)
