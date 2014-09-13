__author__ = 'karinlag'

import Utils

class FibbonachiBreak():
    def __init__(self, genomeLength):
        self.genomeLength = genomeLength

    def _F(self):
        a,b = 0,1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b

    def _subFib(self, startNumber, endNumber):
        for cur in self._F():
            if cur > endNumber:
                return
            if cur >= startNumber:
                yield cur

    def generate(self, startNumber, endNumber):
        return [x for x in self._subFib(startNumber, endNumber)]







if __name__ == "__main__":
    bp = FibbonachiBreak(1000)
    numbers =  bp.generate(200,1000)
    print numbers
    print Utils.calculateN50(numbers)


