class EmailService:
    def __init__(self):
        pass

    def send_email(self, recipient: str, msg: str):
        # Logic to send an email
        print(f"Sending email to {recipient}: {msg}")


class User:
    def __init__(self, username: str) -> None:
        self._username = username
        self.__registered = False

    def register(self):
        if self._username is None:
            raise Exception("Error. username not provided")
        self.__registered = True
        print(f"User: {self._username} properly registered")

    def is_registered(self):
        return self.__registered


class UserManager:
    def __init__(self):
        pass

    def register_user(self, username):
        user = User(username)
        email_service = EmailService()
        # Register user logic
        email_service.send_email(username, "Welcome")
        user.register()
