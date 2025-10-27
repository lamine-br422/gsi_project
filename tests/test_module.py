from module import Module

def test_module_average_and_credit():
    m = Module("MTI", "Methods & Technologies of Implementation",
               coef=3, credit=5, hours_tp=1.5,
               continous_percent=40, exam_percent=60)
    m.set_grade(tp=10, exam=12)
    avg = m.calculate_average()
    credit = m.calculate_credits()
    assert round(avg, 1) == 11.2
    assert credit == 5
