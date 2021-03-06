#######################################################################
# Name: test_pathologic_models
# Purpose: Test for grammar models that could lead to infinite loops are
#   handled properly.
# Author: Igor R. Dejanović <igor DOT dejanovic AT gmail DOT com>
# Copyright: (c) 2014 Igor R. Dejanović <igor DOT dejanovic AT gmail DOT com>
# License: MIT License
#######################################################################

import pytest  # type: ignore

# proj
from arpeggio import *


def test_optional_inside_zeroormore():
    """
    Test optional match inside a zero or more.
    Optional should always succeed thus inducing ZeroOrMore
    to try the match again.
    Arpeggio handle this case.
    """
    def grammar():
        return ZeroOrMore(Optional('a')), EOF

    parser = ParserPython(grammar)

    with pytest.raises(NoMatch):
        # This could lead to infinite loop
        parser.parse('b')
