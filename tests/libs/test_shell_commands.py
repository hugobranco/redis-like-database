import pytest
from libs.shell_commands import command_factory, Get, Command, Numequalto, Set, Unset
from tests.fixtures.factories.redis_storage import RedisStorageFactory
from services import redis_storage_db


@pytest.mark.parametrize(
    "command, key, value, data_type",
    [
        pytest.param("GET", "key", "value", Get, id="Existent command"),
        pytest.param("TEST", "key", "value", Command, id="Non Existent command"),
    ]
)
def test_command_factory(command, key, value, data_type):
    assert isinstance(command_factory(command, key, value), data_type)


@pytest.mark.parametrize(
    "key, value",
    [
        pytest.param("1", "value", id="Get existent key"),
        pytest.param("2", "Key not found", id="Get non existent key"),
    ]
)
def test_execute_get_command(key, value):
    RedisStorageFactory.clean_storage()
    RedisStorageFactory.set_up_storage(key=key, value=value)
    command = Get(key=key, value=value)

    assert command.execute() == value


@pytest.mark.parametrize(
    "value_to_search, total",
    [
        pytest.param("1", 2, id="Existent value"),
        pytest.param("5", 0, id="Non existent value"),
    ]
)
def test_execute_numequalto_command(value_to_search, total):
    RedisStorageFactory.clean_storage()
    RedisStorageFactory.set_up_big_storage()
    command = Numequalto(key="key", value="value")
    command.value_to_search = value_to_search

    assert command.execute() == total


@pytest.mark.parametrize(
    "key, value, return_message, expected_storage",
    [
        pytest.param("2", "value", "", {"1": "value", "2": "value"}, id="Set non existent key"),
        pytest.param("1", "value", "Key already exists. Key value updated", {"1": "value"}, id="Set existent key"),
    ]
)
def test_execute_set_command(key, value, return_message, expected_storage):
    RedisStorageFactory.clean_storage()
    RedisStorageFactory.set_up_storage(key="1", value="value")

    command = Set(key=key, value=value)

    assert command.execute() == return_message
    assert redis_storage_db == expected_storage


@pytest.mark.parametrize(
    "key, return_message, expected_storage",
    [
        pytest.param("5", "Key not found", {"1": "value"}, id="Unset non existent key"),
        pytest.param("1", "", {}, id="Unset existent key"),
    ]
)
def test_execute_unset_command(key, return_message, expected_storage):
    RedisStorageFactory.clean_storage()
    RedisStorageFactory.set_up_storage(key="1", value="value")

    command = Unset(key=key, value="value")

    assert command.execute() == return_message
    assert redis_storage_db == expected_storage
