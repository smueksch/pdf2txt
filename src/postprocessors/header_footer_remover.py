import re


class HeaderFooterRemover:
    """ Removes fixed header and footer. """

    name = 'HeaderFooterRemover'
    desc = 'Remove fixed header and footer'

    def __call__(self, raw_text: str):
        text = re.sub(r'The Raucle Tongue', r'', raw_text)
        text = re.sub(r'translatit by Gavin Douglas and modrenised by John Law', r'', text)
        return text
