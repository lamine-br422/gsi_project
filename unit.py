from module import Module
from academicelement import AcademicElement

class Unit(AcademicElement):
    def __init__(self, name, title, modules=[]):
        super().__init__(name, title)
        self._modules = modules

    def add_module(self, module):
        self._modules.append(module)

    def calculate_average(self):
        if not self._modules:
            return 0
        total = 0
        total_coef = 0
        for m in self._modules:
            total += m.calculate_average() * m.coef
            total_coef += m.coef
        return total / total_coef if total_coef else 0

    def calculate_credits(self):
        if not self._modules:
            return 0
        avg = self.calculate_average()
        if avg >= 10:
            return sum(m.credit for m in self._modules)
        return sum(m.calculate_credits() for m in self._modules)

