from pytest import mark
from pytest_mock import MockFixture

from {{ cookiecutter.project_slug }} import __main__ as main


@mark.unit
def test_init(mocker: MockFixture):
    mock = mocker.patch.object(main, 'main')
    bak = main.__name__
    main.__name__ = '__main__'

    main.init()
    mock.assert_called_once()

    main.__name__ = bak


@mark.unit
def test_main(mocker: MockFixture):
    mock = mocker.patch.object(main, 'print')
    main.main(['--print'])
    mock.assert_called_once()
