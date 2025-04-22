import pytest
import salt.modules.test as testmod

import saltext.test_salt_winrepo.modules.test_salt_winrepo_mod as test_salt_winrepo_module


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"test.echo": testmod.echo},
    }
    return {
        test_salt_winrepo_module: module_globals,
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    assert test_salt_winrepo_module.example_function(echo_str) == echo_str
