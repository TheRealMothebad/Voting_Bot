

class ballot:
    def __init__(self, voter) -> None:
        self.voter = voter
        self.scores = {}
    
    @staticmethod
    def final(tab, ballots):
        can1 = [tab.index(0).value(), 0]
        can2 = [tab.index(1).value(), 0]
        same = 0
        print(can1)
        for i in ballots:
            highest = i.highest(can1, can2)
            if highest == can1[0]:
                can1[1] += 1
            elif highest == can2[0]:
                can2[1] += 1
            elif highest == "same":
                same += 1
            else:
                print("ERROR: bad ballot result")
        return {can1[0] : can1[1], can2[0] : can2[1], "same" : same}
        '''
        if can1[1] > can2[1]:
            return can1[0]
        elif can1[1] < can2[1]:
            return can2[0]
        elif can1[1] == can2[1]:
            return same
        '''




    def highest(self, can1, can2):
        tab1 = self.tabulation[can1]
        tab2 = self.tabulation[can2]
        out = can1 if tab1 > tab2 else (can2 if tab1 < tab2 else ("same" if tab1 == tab2 else -1))
        print(out)
        return out

