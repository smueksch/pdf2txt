import os
import sys
import PyPDF2


class PDFExtractor:
    """ Text extractor for PDF files.

    Attributes:
        in_ (str): Input filename (PDF)
        out (str): Output filename, generally text file.
        post_processors (list): List of post-processors (objects) called on the
            raw extracted text.
        flaggers (list) List of flaggers (objects) to raise warnings on
            processed string.
    """

    def __init__(self, in_: str = '', out: str = '', post_processors: list = [],
                 flaggers: list = []) -> None:
        """ Initialize extractor.

        Note that order of post-processors matters. Applied in sequence, ones
        that are more restrictive in what they process should come first.
        Flaggers are applied after all post-processors are run.

        Args:
            in_ (str, optional): Filename of input file (PDF), defaults to ''.
            out (str, optional): Filename of output file, generally text file,
                defaults to ''.
            post_processors (list, optional): List of post-processors applied to
                the text after extraction, defaults to []
            flaggers (list, optional): List of flaggers to print warnings
                concerning the extracted text, defaults to [].
        """
        self.in_ = in_
        self.out = out
        self.text = ''
        self.post_processors = post_processors
        self.flaggers = flaggers

    def run_post_processors(self, raw_text: str) -> str:
        """ Run all post processors in sequence.

        Args:
            raw_text (str): Text to be processed.

        Returns:
            str: Processed text.
        """
        text = raw_text

        for post_processor in self.post_processors:
            text = post_processor(text)

        return text

    def run_flaggers(self, text: str) -> None:
        """ Flag content for human post processing.

        Args:
            text (str): Processed text to potentially raise flags on.
        """
        for flagger in self.flaggers:
            flagger(text)

    def extract(self, in_: str = '') -> None:
        """ Extract text from PDF.

        Args:
            in_ (str, optional): Input filename (PDF), defaults to self.in_.
        """
        in_filename = in_ if in_ != '' else self.in_

        try:
            with open(in_filename, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                raw_text = ''

                for i in range(pdf_reader.numPages):
                    raw_text = raw_text + pdf_reader.getPage(i).extractText()

                self.text = self.run_post_processors(raw_text)
                self.run_flaggers(self.text)
        except FileNotFoundError as err:
            if in_filename == '':
                error_msg = 'Error: Abort reading. No input file specified.'
            else:
                error_msg = 'Error: Abort reading. Couldn\'t find {in_}'
            print(error_msg.format(in_=in_filename), file=sys.stderr,
                  flush=True)

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
