from dependency_injection.with_di import User, UserManager, EmailService


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


# Tests on UserManager now can be easily implemented:
def test_user_registration():
    user = User("oopazo")
    email_service = EmailService()
    manager = UserManager()
    # Injecting dependencies to UserManager:
    manager.register_user(user, email_service)
    assert user.is_registered()


def test_user_registration_2():
    user = User("oopazo")
    email_service = EmailService()
    manager = UserManager()
    # Injecting dependencies to UserManager:
    assert user.is_registered() is False
    manager.register_user(user, email_service)
    assert user.is_registered() is True
