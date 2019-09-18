"""
The CLI entry of {{ cookiecutter.project_name }}.
"""
from argparse import ArgumentParser

from ._version import __version__ as version


def main(argv=None):
    """
    {{ cookiecutter.project_short_description }}
    """
    parser = ArgumentParser()
    parser.description = main.__doc__
    parser.add_argument(
        '-p', '--print', action='store_true', help='print hello world'
    )
    parser.add_argument('-V', '--version', action='version', version=version)
    args = parser.parse_args(argv)
    if args.print:
        print("Hello world!")


def init():
    """
    This is a wrapper for unit test only.
    """
    if __name__ == '__main__':
        main()


init()
