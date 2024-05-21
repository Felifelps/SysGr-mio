import pytest

from source.control import Control

@pytest.fixture
def control_obj():
    return Control()
