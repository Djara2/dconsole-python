import math
class dnum:
    def __init__(self, c, v, e):
        self.coefficient = c
        self.value = v
        self.exponent = e
    @property
    def coefficient(self):
        return self._coefficient
    @coefficient.setter
    def coefficient(self, value):
        self._coefficient = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, arg):
        self._value = arg
    @property
    def exponent(self):
        return self._value
    @exponent.setter
    def exponent(self, value):
        self._exponent = value
    def evaluate(self):
        resultant = math.pow(self.value, self.exponent)
        print("resultant = {}".format(resultant))
        resultant = resultant * self.coefficient
        print("resultant = {}".format(resultant))
        return resultant
    def add(num1, num2):
        evaluatedNum1 = num1.evaluate()
        evaluatedNum2 = num2.evaluate()
        out = evaluatedNum1 + evaluatedNum2
        return out
    def sub(num1, num2):
        evaluatedNum1 = num1.evaluate()
        evaluatedNum2 = num2.evaluate()
        out = evaluatedNum1 - evaluatedNum2
        return out
