import pytest
import brownie
from brownie import accounts, SimpleStorage


@pytest.fixture
def simple_storage():
    simple_storage = SimpleStorage.deploy({"from": accounts[0]})
    simple_storage.tx.wait(1)
    # Assert
    assert simple_storage is not None
    return simple_storage


def test_setNumber_to_zero_reverts(simple_storage):
    with brownie.reverts("invalid number"):
        simple_storage.setNumber(0)


def test_setNumber(simple_storage):
    # Arrange
    account = accounts[0]
    expected = 777

    # Act
    tx = simple_storage.setNumber(expected, {"from": account})
    tx.wait(1)

    # Assert
    assert simple_storage.number() == expected


def test_setNumber_emits_event(simple_storage):
    tx = simple_storage.setNumber(777)
    # Check log contents
    assert len(tx.events) == 1
    assert tx.events[0]['oldNum'] == 0
    assert tx.events[0]['newNum'] == 777
