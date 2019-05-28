class Match:
    """Holds the data about signle match."""

    def __init__(self, team1, team2):
        self.team2 = team2
        self.team1 = team1

    def __str__(self):
        return self.team1 + " vs " + self.team2
