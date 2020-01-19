import re


class HyphenFixer:
    """ Replace wrongly extrhyphen_fixer.pyacted hyphens with proper ones. """

    name = 'HyphenFixer'
    desc = 'Replace wrongly extracted hyphens with proper ones'

    def __call__(self, raw_text: str):
        text = re.sub(u'Ð', r'-', raw_text)
        return re.sub(u'–', r'-', text)
