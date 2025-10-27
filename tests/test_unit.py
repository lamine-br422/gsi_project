from module import Module
from unit import Unit

def test_unit_average_and_credit():
    m1 = Module("MTI", "Methods", coef=3, credit=5)
    m1.set_grade(tp=10, exam=12)
    m2 = Module("AABD", "Database", coef=2, credit=4)
    m2.set_grade(tp=8, exam=6)
    u = Unit("UEM11", "UE Méthodologie", [m1, m2])
    avg = u.calculate_average()
    credit = u.calculate_credits()
    assert round(avg, 1) == 9.6
    assert credit == 0  # car moyenne < 10
