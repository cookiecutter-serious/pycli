#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup the package {{ cookiecutter.project_name }}"""

from runpy import run_path

from setuptools import find_packages, setup

_INFO = run_path('src/{{ cookiecutter.project_slug }}/_meta.py')

setup(
    author=_INFO['__author__'],
    author_email=_INFO['__email__'],
    url=_INFO['__home__'],

    use_scm_version=True,
    zip_safe=False,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': (
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.__main__:main',
        ),
    },

    python_requires='>=3.4',
    install_requires=[

    ],
    setup_requires=[
        'pytest-runner',
        'setuptools_scm',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-pep8',
        'pytest-flakes',
        'pytest-mock',
        'mock',
    ],

    keywords=['CLI'],
    platforms=['any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
