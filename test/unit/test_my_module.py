from unittest.mock import patch

from project_name.my_module import MyModule, main


def test_my_function():
    MyModule.my_function()


@patch('project_name.my_module.MyModule.my_function')
def test_main(mock_my_function):
    main()
    mock_my_function.assert_called_once()
