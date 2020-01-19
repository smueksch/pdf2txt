from number_flagger import NumberFlagger
from footnote_flagger import FootnoteFlagger
from stray_letter_flagger import StrayLetterFlagger

# List of available flagger classes. Here so post-processors can be
# programmatically instantiated.
__flaggers = [NumberFlagger,
              FootnoteFlagger,
              StrayLetterFlagger]

flaggers = {f.name: f for f in __flaggers}
__all__ = list(flaggers.keys())
