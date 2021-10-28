import candidate
import ballot

class election:
    active = None
    def __init__(self, candidates) -> None:
        self.candidates = []
        self.ballots = {}
        self.tabulation = {}

class STAR(election):
    def __init__(self, candidates) -> None:
        super().__init__(candidates)
    
    def vote(self, msg):
        createBallot = True
        for i in election.active.ballots:
            if i.voter == msg.author:
                createBallot = False
                break
        if createBallot:
            election.active.ballots.append({msg.author : ballot(msg.author)})
        for i in range(0, msg, 2):
            election.active.scores[msg.author].update({msg[i] : msg[i+1]})
    
    def tabulate(self):
        for i in self.ballots:
            if ballot.candidate not in self.tabulation:
                self.tabulation.append(ballot.candidate)
                self.tabulation[ballot.candidate] = 0
            self.tabulation[ballot.candidate] += ballot.score
        self.tabulation = dict(sorted(self.tabulation.items(), key=lambda x:x[1], reverse=True))
    


