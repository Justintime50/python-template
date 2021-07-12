import mock
from project_name.my_module import (
    main,
    MyModule
)


def test_my_function():
    MyModule.my_function()


@mock.patch('project_name.my_module.MyModule.my_function')
def test_main(mock_my_function):
    main()
    mock_my_function.assert_called_once()
