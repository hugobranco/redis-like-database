import pytest
from services.console import Console
from tests.fixtures.factories.console_service import ConsoleServiceFactory


@pytest.mark.parametrize(
    "console_obj, inserted_command, command_value",
    [
        pytest.param(Console(), "SET", "SET", id="Command only one value"),
        pytest.param(Console(), "GET key", "GET", id="Existent command"),
        pytest.param(Console(), "", "", id="Empty command"),
        pytest.param(Console(), 1, "", id="Command is integer type")
    ]
)
def test_get_shell_inserted_command(console_obj, inserted_command, command_value):
    console_obj.get_shell_inserted_command(inserted_command=inserted_command)

    assert console_obj.command == command_value



@pytest.mark.parametrize(
    "console_obj, valid_command",
    [
        pytest.param(
            ConsoleServiceFactory.set_up_console(command="SET", key="key", value="value"),
            True,
            id="Existent command"
        ),
        pytest.param(
            ConsoleServiceFactory.set_up_console(command="WRONG", key="key", value="value"),
            False,
            id="Non Existent command"
        ),
        pytest.param(
            ConsoleServiceFactory.set_up_console(command="", key="", value=""),
            False,
            id="Empty string command"
        ),
        pytest.param(
            ConsoleServiceFactory.set_up_console(command=1, key="", value=""),
            False,
            id="Command a int value"
        ),
        pytest.param(
            ConsoleServiceFactory.set_up_console(command=None, key="", value=""),
            False,
            id="Command None value"
        ),
    ]
)
def test_execute_command(console_obj, valid_command):
    response_value = console_obj.execute_command()

    if(valid_command):
        assert (response_value == "")
    else:
        assert (response_value == "error")
