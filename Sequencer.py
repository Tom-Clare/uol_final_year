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

    # need a way to dictate how the clock in is done
    def clock_in(self, clock_input):
        self.clock_input.bind_to(self.measure)
        self._clock_in = 0


    def measure(self, input):
        # if current == new, nothing
        # if current != new, update current

        if self._clock_in != input:
            self._clock_in = input
            if self._clock_in == 1:
                self.next()
        

