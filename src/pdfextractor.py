import os
import sys
import re
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.pdfdevice import PDFDevice  # TODO: Do I need this?
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


# TODO: Massively refactor this code...make it closer to the pdfextractor-OLD
class PDFExtractor:

    def __init__(self,
            in_: str = '', out: str = '', post_processors: list = [],
            flaggers: list = [],
            password='',
            encoding='utf-8',
            normalize_spaces=True,
            caching=True,
            detect_vertical=True,
            char_margin=1.0,
            line_margin=0.3,
            word_margin=0.3):
        """PDF Text extractor

        password: password for password protected file
        encoding: expected encoding
        normalize_spaces: convert multiple spaces to a single space
        caching: activate PDFMIner object caching
        detect_vertical: detect vertical text

        For more details about the options, see:
            http://www.unixuser.org/~euske/python/pdfminer/index.html

        """
        self.in_ = in_
        self.out = out
        self.text = ''
        self.post_processors = post_processors
        self.flaggers = flaggers
        self.password = password
        self.encoding = encoding

        self.normalize_spaces = normalize_spaces

        self.caching = caching

        self.laparams = LAParams()
        self.laparams.detect_vertical = detect_vertical
        self.laparams.char_margin = char_margin
        self.laparams.line_margin = line_margin
        self.laparams.word_margin = word_margin

    # TODO: Why does this not simply use self.text?
    def run_post_processors(self, raw_text: str) -> str:
        """ Run all post processors in sequence.

        Args:
            raw_text (str): Text to be processed.

        Returns:
            str: Processed text.
        """
        text = raw_text

        # TODO: why is the __call__ function not a classmethod/staticmethod?
        for post_processor in self.post_processors:
            pp = post_processor()
            text = pp(text)

        return text

    # TODO: Why does this not simply use self.text?
    def run_flaggers(self, text: str) -> None:
        """ Flag content for human post processing.

        Args:
            text (str): Processed text to potentially raise flags on.
        """
        # TODO: why is the __call__ function not a classmethod/staticmethod?
        for flagger in self.flaggers:
            f = flagger()
            f(text)

    # Literally taken from pdf2text PDFMiner wrapper.
    def extract(self, in_: str = '') -> None:
        """ Extract text from PDF.

        Args:
            in_ (str, optional): Input filename (PDF), defaults to self.in_.
        """
        in_filename = in_ if in_ != '' else self.in_

        with open(in_filename, 'rb') as stream:
            # Prepare pdf extraction
            outfp = StringIO()
            rsrcmgr = PDFResourceManager(caching=self.caching)
            device = TextConverter(
                    rsrcmgr,
                    outfp,
                    #codec=self.encoding,
                    laparams=self.laparams,
            )

            # Extract text
            process_pdf(
                    rsrcmgr,
                    device,
                    stream,
                    set(), # pagenos
                    maxpages=0,
                    password=self.password,
                    caching=self.caching,
                    check_extractable=True,
            )

            # Output
            self.text = outfp.getvalue()
            outfp.close()
            if self.normalize_spaces:
                self.text = re.sub(r'  +', ' ', self.text)

            self.text = self.run_post_processors(self.text)
            self.run_flaggers(self.text)

    def write(self, out: str = '', force: bool = False) -> None:
        """ Write extracted and processed text to file.

        Writes the extracted and processed text to file if and only if the
        output file either does not exist or force is set to True.

        Args:
            out (str, optional): Output filename, generally text file, defaults
                to self.out.
            force (bool, optional): Flag to determine whether writing to file
                should be forced, defaults to False.
        """
        out_filename = out if out != '' else self.out

        if force or not os.path.isfile(out_filename):
            try:
                with open(out_filename, 'w') as f:
                    f.write(self.text)
            except FileNotFoundError as err:
                if out_filename == '':
                    error_msg = 'Error: Abort writing. No output file specified.'
                else:
                    error_msg = 'Error: Abort writing. Couldn\'t find {out}'
                print(error_msg.format(out=out_filename), file=sys.stderr,
                      flush=True)
        else:
            error_msg = 'Error: Abort writing to {out}. File exists and force' \
                        ' flag is not set.'
            print(error_msg.format(out=out_filename), file=sys.stderr,
                  flush=True)