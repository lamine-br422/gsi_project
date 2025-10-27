import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from module import Module
from unit import Unit
from semester import Semester

def test_semester_average_and_credits():
    m1 = Module("MTI", "Methods", coef=3, credit=5)
    m1.set_grade(tp=10, exam=12)
    m2 = Module("AABD", "Database", coef=2, credit=4)
    m2.set_grade(tp=8, exam=6)
    u = Unit("UEM11", "Méthodologie", [m1, m2])
    s = Semester("S1", "Semestre 1", [u])
    avg = s.calculate_average()
    credits = s.calculate_credits()
    assert isinstance(avg, float)
    assert isinstance(credits, int)
