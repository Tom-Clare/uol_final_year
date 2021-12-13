class Sequencer():
    def __init__(self, length = 8):
        self._sequence = [0] * length
        self._index = 0
        self._out = self._sequence[self._index]

    def setSequence(self, index, value):
        self._sequence[index - 1] = value
        self.update() #in case current value has been changed

    def next(self):
        self._index = self._index + 1
        self.update()

    def update(self):
        self._out = self._sequence[self._index]