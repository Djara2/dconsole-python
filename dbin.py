class dbin:
    def __init__(value):
        self.bits = bin(value)
        self.value = value
    @property
    def bits(self):
        return self._bits
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, arg):
        self._value = arg
        self._bits = bin(self.value)
