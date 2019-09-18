"""Read the version from installed package"""
from pkg_resources import get_distribution

__version__ = get_distribution(__package__).version
