import time

class Clock(object):

    def __init__(self, bpm = 120):
        self._bpm = bpm
        self._observers = []
        self.start()

    def start(self):
        self._status = 1
        self.out = 1
        print("clock high")

        ## currently, the entire process gets stuck in this loop and nothing else can continue
        while self._status == 1:
            interval = self._bpm / 60
            time.sleep(interval / 2)
            self.out = 0
            print("clock low")
            time.sleep(interval / 2)
            self.out = 1
            print("clock high")

    @property
    def out(self):
        return self._out

    @out.setter
    def out(self, value):
        self._out = value
        print("value changed")
        for callback in self._observers:
            print("announcing change")
            callback(self._out)
    
    def bind_to(self, callback):
        print("binding")
        self._observers.append(callback)
