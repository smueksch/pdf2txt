import re


class QuotationFixer:
    """ Replace wrongly extracted single and double quotes with proper ones. """

    name = 'QuotationFixer'
    desc = 'Replace wrongly extracted quotes with proper ones'

    def __call__(self, raw_text: str):
        text = re.sub(u'“', r'"', raw_text)
        text = re.sub(u'”', r'"', text)
        text = re.sub(u'‘', r"'", text)
        text = re.sub(u'’', r"'", text)
        return text
