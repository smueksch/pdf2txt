import re


class WordNumFixer:
    """ Remove numbers directly at the beginning or end of words.

    E.g. 14Thor -> Thor
         halo3  -> halo

    Sensible, as words are very unlikely to appear with numbers in that way.
    Should take care of left-over footnotes (e.g. halo3) and stray page numbers
    (e.g. 14Thor).
    """

    name = 'WordNumFixer'
    desc = 'Remove numbers directly at the beginning or end of words'

    def __call__(self, raw_text: str):
        text = raw_text

        # Remove numbers at start of words.
        before_regex = r'([0-9]+)([A-Za-z]+)'
        match = re.search(before_regex, raw_text)
        while match:
            text = text[:match.start(1)] + text[match.end(1):]
            match = re.search(before_regex, text)

        # Remove numbers at end of words and punctuation.
        # NOTE: Removing numbers directly attached after a punctuation, e.g.
        #       '.90' is based on the assumption that the text is well formatted,
        #       i.e. the author put spaces in after punctuation marks.
        #after_regex = r'([A-Za-z,]+)([0-9]+)'
        after_regex = r'([A-Za-z,;.?!\'":]+)([0-9]+)'
        match = re.search(after_regex, text)
        while match:
            text = text[:match.start(2)] + text[match.end(2):]
            match = re.search(after_regex, text)

        return text
