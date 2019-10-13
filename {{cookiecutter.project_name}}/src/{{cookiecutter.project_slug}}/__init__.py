"""{{ cookiecutter.project_short_description }}"""

from .__main__ import main
from ._meta import __author__, __copyright__, __email__, __home__
from ._version import __version__

__all__ = [
    '__author__',
    '__copyright__',
    '__email__',
    '__home__',
    '__version__',
    main.__name__,
]
