from academicelement import AcademicElement
from unit import Unit

class Semester(AcademicElement):
    def __init__(self, name, title, units=[]):
        super().__init__(name, title)
        self._units = units

    def add_unit(self, unit):
        self._units.append(unit)

    def calculate_average(self):
        if not self._units:
            return 0
        total = 0
        total_coef = 0
        for u in self._units:
            coef_u = sum(m.coef for m in u._modules)
            total += u.calculate_average() * coef_u
            total_coef += coef_u
        return total / total_coef if total_coef else 0

    def calculate_credits(self):
        if not self._units:
            return 0
        avg = self.calculate_average()
        if avg >= 10:
            return sum(m.credit for u in self._units for m in u._modules)
        return sum(u.calculate_credits() for u in self._units)
