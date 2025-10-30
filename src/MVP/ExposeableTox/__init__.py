'''Info Header Start
Name : __init__
Author : Wieland PlusPlusOne@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.12480
Info Header End'''

from pathlib import Path

# The __init__.py file needs to be located next to the toxfile.
ToxFile = Path( Path(  __file__ ).parent, "ExposeableTox.tox" )

# If several components want to instanciate this ToxFile, but only one is required in the project,
# this member allows for a clearly defined global op shortcut.
DefaultGlobalOpShortcut = "A897a62dd-8653-4feb-b0b8-94070756566d"


from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
  # This allows for importing Typing without having to import and instanciate the object an additional time.
    from .extExposeableExtension import extExposeableExtension
    Typing = Union[
        extExposeableExtension
    ]
else:
    Typing = None

# Make sure to only export required members.
__all__ = ["ToxFile", "Typing", "DefaultGlobalOpShortcut"]