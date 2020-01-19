from header_footer_remover import HeaderFooterRemover
from double_newline_fixer import DoubleNewlineFixer
from excessive_newline_remover import ExcessiveNewlineRemover
from quotation_fixer import QuotationFixer
from hyphen_fixer import HyphenFixer
from footnote_remover import FootnoteRemover
from number_only_line_remover import NumberOnlyLineRemover
from word_num_fixer import WordNumFixer
from eol_space_remover import EOLSpaceRemover
from bullet_point_fixer import BulletPointFixer
from unknown_char_fixer import UnknownCharFixer

# List of available post-processor classes. Here so post-processors can be
# programmatically instantiated.
__pps = [HeaderFooterRemover,
         DoubleNewlineFixer,
         ExcessiveNewlineRemover,
         QuotationFixer,
         HyphenFixer,
         FootnoteRemover,
         NumberOnlyLineRemover,
         WordNumFixer,
         EOLSpaceRemover,
         BulletPointFixer,
         UnknownCharFixer]

post_processors = {pp.name: pp for pp in __pps}
__all__ = list(post_processors.keys())
