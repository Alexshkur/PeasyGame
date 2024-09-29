class AI:
    def __init__(self, Balances):
        print("AIMode - simply and fast library for creating AI")
        self.balances = Balances

    def multLayer(self, inputNodes, layer):
        Result = []
        for neuron in layer:
            balance = []
            for i, node in enumerate(neuron):
                balance.append(inputNodes[i] * node)
            result = sum(balance)
            Result.append(result)
        return tuple(Result)

    def tick(self, inputNodes):
        LastInput = inputNodes
        for balance in self.balances:
            LastInput = self.multLayer(LastInput, balance)
        return LastInput