__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__home__ = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}'
__copyright__ = 'Copyright (C) 2017 ' + __author__


def _get_version(default='x.x.x.dev'):
    try:
        from pkg_resources import DistributionNotFound, get_distribution
    except ImportError:
        return default
    else:
        try:
            return get_distribution(__package__).version
        except DistributionNotFound:  # Run without install
            return default
        except ValueError:  # Python 3 setup
            return default
        except TypeError:  # Python 2 setup
            return default


__version__ = _get_version()
