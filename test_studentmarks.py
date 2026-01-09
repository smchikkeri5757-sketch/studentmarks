import unittest
from studentmarks import calculate_grade


class TestStudentMarks(unittest.TestCase):

    def test_grade_s(self):
        self.assertEqual(calculate_grade([95, 92, 90]), "S")

    def test_grade_a(self):
        self.assertEqual(calculate_grade([85, 82, 80]), "A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade([70, 75, 65]), "B")

    def test_grade_c(self):
        self.assertEqual(calculate_grade([55, 60, 50]), "C")

    def test_grade_d(self):
        self.assertEqual(calculate_grade([45, 42, 48]), "D")

    def test_grade_f(self):
        self.assertEqual(calculate_grade([30, 35, 38]), "F")


if __name__ == "__main__":
    unittest.main()
