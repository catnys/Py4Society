class User:
    def __init__(self, username, password):
        """Self constructor for the user."""
        self.username = username
        self.password = password  # Note: Storing plain text passwords is not secure.

    def set_password(self, new_password):
        """Set a new password for the user."""
        self.password = new_password

    def check_password(self, password):
        """Check if the provided password matches the stored password."""
        return self.password == password

    def __str__(self):
        return f"User({self.username})"
