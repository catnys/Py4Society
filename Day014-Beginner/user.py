class User:
    def __init__(self, username, password, score=0):
        """Constructor for the User class with an optional score parameter."""
        self.username = username
        self.score = score
        self.password = password

    def getUsername(self):
        """Getter for the username."""
        return self.username

    def setUsername(self, username):
        """Setter for the username."""
        self.username = username

    def getScore(self):
        """Getter for the score."""
        return self.score

    def setScore(self, score):
        """Setter for the score."""
        self.score = score

    def setPassword(self, new_password):
        """Set a new password for the user."""
        self.password = new_password

    def getPassword(self):
        return self.password

    def __str__(self):
        return f"{self.username},{self.password},{self.score}"
