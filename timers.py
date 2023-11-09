

class Timer:
    timers = []

    def __init__(self, miliseconds, callback, arguement = None):
        self.time = 0
        self.callback = callback
        self.arguement = arguement
        self.max_time = miliseconds
        self.isTicking = False

        Timer.timers.append(self)

    def tickTimers(miliseconds):
        for timer in Timer.timers:
            if timer.isTicking:
                timer.removeTime(miliseconds)

    def beginTicking(self):
        self.isTicking = True
        self.time = self.max_time

    def setTime(self, miliseconds: float):
        self.time = miliseconds

    def removeTime(self, miliseconds):
        self.time -= miliseconds
        if self.time <= 0:
            self.isTicking = False
            self.doCallback()

    def doCallback(self):
        if self.arguement == None:
            self.callback()
        else:
            self.callback(self.arguement)