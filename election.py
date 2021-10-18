import candidate

class election:
    active = None
    def __init__(self, candidates) -> None:
        self.tabulation = {}
        self.ballots = []

class STAR(election):
    def __init__(self, candidates) -> None:
        super().__init__(candidates)
    


