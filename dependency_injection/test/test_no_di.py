from io import StringIO
import sys
from dependency_injection.no_di import *


def test_user_1():
    user = User("oopazo")
    assert user._username == "oopazo"


def test_user_2():
    user = User("oopazo")
    assert user.is_registered() is False


def test_user_register():
    user = User("oopazo")
    user.register()
    assert user.is_registered() is True


def test_user_registration():
    manager = UserManager()
    manager.register_user("oopazo")
    # How can I implement tests on UserManager???
