#CaEn
class CalcEngine:
    def __init__(self):
        self.result = 0

#   тело деструктора.
    def __del__(self):
        self.result = 0
        print('Destructor called, CalcEngine freed.')

    def add(self, a, b):
        self.result = a + b
        return self.result

    def add(self, a):
        self.result += a
        return self.result

    def sub(self, a, b):
        self.result = a - b
        return self.result


    def sub(self, a):
        self.result -= a
        return self.result


    def mul(self, a, b):
        self.result = a * b
        return self.result


    def div(self, a, b):
        self.result = a / b
        return self.result


    def percent(self, a, b):
        self.result = a * b / 100
        return self.result


