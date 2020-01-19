import re


class BulletPointFixer:
    """ Replace Unicode bullet point with asterisk (*). """

    name = 'BulletPointFixer'
    desc = 'Replace Unicode bullet point with asterisk (*)'

    def __call__(self, raw_text: str) -> str:
        text = re.sub(u'●', r'*', raw_text)
        return re.sub(u'•', r'*', text)
