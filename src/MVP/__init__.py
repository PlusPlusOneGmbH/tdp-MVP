'''Info Header Start
Name : __init__
Author : Wieland PlusPlusOne@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.12480
Info Header End'''

from . import ExposeableTox

__minimum_td_version__ = "2023.1200"

# Futureprrofing for automated search of toxfiles and imports.
_ToxFiles = {
    "ExposeableTox" : ExposeableTox.ToxFile
}