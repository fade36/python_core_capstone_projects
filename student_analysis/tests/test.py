import unittest
from src.analysis import get_student, get_avg, top_ten, filterr


class TestAnalysis(unittest.TestCase):

    def setUp(self):
        self.students = [
            {"G1": 10, "G2": 12, "G3": 15, "school": "GP"},
            {"G1": 15, "G2": 16, "G3": 18, "school": "MS"},
            {"G1": 8, "G2": 9, "G3": 10, "school": "GP"}
        ]

    def test_get_student(self):
        self.assertEqual(get_student(self.students, 0), self.students[0])

    def test_get_nonexistent_student(self):
        self.assertIsNone(get_student(self.students, 10))

    def test_get_avg(self):
        self.assertEqual(get_avg(self.students)["G3"], 14.33)

    def test_top_ten(self):
        self.assertEqual(top_ten(self.students)[0]["G3"], 18)

    def test_filter_students(self):
        result = filterr(self.students, {"school": ["GP"]})
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()