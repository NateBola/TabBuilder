from dataclasses import dataclass
from enum import IntEnum

class NoteDurations(IntEnum):
    WHOLE = 0
    HALF = 1
    QUARTER = 2
    EIGHTH = 3
    SIXTENTH = 4
    TRIPLE = 5

@dataclass
class TabStaff():
    pass

@dataclass
class TabNote():
    # for tab string, low E string is string 0, high E is 6
    # for tab fret, 0 represents open string
    # for tab spacing, 0 is the smallest incriment
    # for tab backset, positive numbers back set the note on the tab to show chords
    tab_string: int
    tab_fret: int
    tab_spacing: int
    tab_backset: int

# Example of an A5 power chord on the bottom E, A, and D strings
note1 = TabNote(0, 5, 0, 0)
note2 = TabNote(1, 7, 0, 1)
note3 = TabNote(2, 7, 0, 2)