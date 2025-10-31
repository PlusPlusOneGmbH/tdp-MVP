# tdp MVP
### TDP stands for TouchDesignerPackage
This repository deminstrates a project that can be packaged, uploaded and installes to and from PyPi using PIP, uv or similiar and be used in TouchDesigner

## Naming
Packages start with __-tdp__ to be easily identifable and searchable on the package index. 

The TopLevel-Module omits the dash in favor no-seperator at all.

__Package-Name:__ tdp-MVP

__TopLevel Module Name:__ tdpMVP

TDP implements a number of required members to be working. They do not follow default python naming and use CamelCase instead to adhere to the default TouchDesigner naming conventions.

## Comp Package
```python
from pathlib import Path

# The __init__.py file needs to be located next to the toxfile.
ToxFile = Path( Path(  __file__ ).parent, "TargetTox.tox" )

# If several components want to instanciate this ToxFile, but only one is required in the project,
# this member allows for a clearly defined global op shortcut.
DefaultGlobalOpShortcut = "TARGETGLOBAL"


from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
  # This allows for importing Typing without having to import and instanciate the object an additional time.
    from .extExtensionFile import extExtensionClass
    Typing = Union[
        extExtensionClass
    ]
else:
    Typing = None

# Make sure to only export required members.
__all__ = ["ToxFile", "Typing", "DefaultGlobalOpShortcut"]

```
## Comp Collection
In the case of deploying several components in the same package, a package can be a collection.

Make sure to import all sub-componente-modules in the root ```__init__.py```  file and add the following members.
```python
# Makre sure subpackages are imported so they can be accesses via the mod. method.
from . import ToxModuleOne
from . import ToxModuleTwo

# Future Proofing
__minimum_td_version__ = "2023.1200"

# Futureprrofing for automated search of toxfiles and imports.
_ToxFiles = {
    "ToxModuleOne" : ToxModuleOne.ToxFile,
    "ToxModuleTwo" : ToxModuleTwo.ToxFile
}
```

This allows the use of TouchDesigner ```mod``` functionality, otherwise you would  not be able to refference submodules.

## Usage
```mod.tdpPackageName.ToxModuleOne.ToxFile``` in the externaltox path of any COMP to fetch the path.

## Notes
Make sure that your Components are set to __Relative to External COMP File (.tox)__ and the paths to external files are aso set acordingly.

Keep as much of your python externalised in .py files to alow for good typehinting.

TouchDesigner and Python behave differently when importing. If you require relative imports to work in TD and to be importable, you will need to do the following check:
```python
if __package__ is None:
  # This means we are in TouchDesigner and we use the TD-Based rules of importing.
  # https://docs.derivative.ca/MOD_Class
	import DatNextToThis
else:
  # We are in package-world. Here we need to specificy that we want to import from a file relative to our current position.
	from . import DatNextToThis
```

## Examples

https://github.com/PlusPlusOneGmbH/tdp-QrCodeCOMP

https://github.com/PlusPlusOneGmbH/TauCeti





