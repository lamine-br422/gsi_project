from module import Module
from unit import Unit
from semester import Semester

def test_semester_average_and_credit():
    m1 = Module("MTI", "Methods", coef=3, credit=5)
    m1.set_grade(tp=10, exam=12)
    m2 = Module("AABD", "Database", coef=2, credit=4)
    m2.set_grade(tp=8, exam=6)
    u = Unit("UEM11", "UE Méthodologie", [m1, m2])
    s = Semester("S1", "Semester 1", [u])
    avg = s.calculate_average()
    credit = s.calculate_credits()
    assert isinstance(avg, float)
    assert isinstance(credit, int)

