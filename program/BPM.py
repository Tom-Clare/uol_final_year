from time import sleep
import threading

class BPM:
    def __init__(self, rate, func_next):
        self._rate = rate
        self._duration = 60 / self._rate 
        self._func_next = func_next # this must be given as a list

        self.heartrate = threading.Thread(name="heartbeat", target=self.go, daemon=True)
        self.heartrate.start()
        

    def go(self):
        counter = 0

        threshold = 1
        while(True):
            
            if threshold:
                counter += 1
                # make callbacks
                for func_next in self._func_next:
                    func_next()
                threshold = 0
            else:
                sleep(self._duration)
                threshold = 1