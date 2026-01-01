import pytest
from student import get_student_result

def test_student_grade_A():
    name = "swapna"
    dept = "bca"
    semester = "3"
    m1 = 97
    m2 = 89
    m3 = 90

    expected_output = (
        "Name: swapna, Department: bca, Semester: 3, "
        "Average: 92.00, Grade: S"
    )

    result = get_student_result(name, dept, semester, m1, m2, m3)

    assert result == expected_output
