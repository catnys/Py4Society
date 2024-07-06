class User:
    def __init__(self, name, total_score, scores):
        self.name = name
        self.total_score = total_score
        self.scores = scores

    def __repr__(self):
        return f"User(name={self.name}, total_score={self.total_score}, scores={self.scores})"
