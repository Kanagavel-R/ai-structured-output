import unittest
from pydantic import ValidationError
from main import Student, get_valid_data


class TestStructuredOutput(unittest.TestCase):

    # Test 1: Valid student data
    def test_valid_data(self):
        data = {
            "name": "Arun",
            "age": 20,
            "skill": "Java",
            "experience_level": "Beginner"
        }

        student = Student(**data)

        self.assertEqual(student.name, "Arun")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.skill, "Java")
        self.assertEqual(student.experience_level, "Beginner")

    # Test 2: Invalid student data
    def test_invalid_data(self):
        data = {
            "name": "Arun",
            "age": -20,
            "skill": "Java",
            "experience_level": "Beginner"
        }

        with self.assertRaises(ValidationError):
            Student(**data)

    # Test 3: Retry succeeds on third attempt
    def test_retry_success(self):
        responses = [
            {
                "name": "Arun",
                "age": -20,
                "skill": "Java",
                "experience_level": "Beginner"
            },
            {
                "name": "Arun",
                "age": 120,
                "skill": "Python",
                "experience_level": "Beginner"
            },
            {
                "name": "Arun",
                "age": 20,
                "skill": "Java",
                "experience_level": "Beginner"
            }
        ]

        result = get_valid_data(responses)

        self.assertEqual(result.age, 20)
        self.assertEqual(result.name, "Arun")

    # Test 4: All three attempts fail
    def test_retry_failure(self):
        responses = [
            {
                "name": "Arun",
                "age": -20,
                "skill": "Java",
                "experience_level": "Beginner"
            },
            {
                "name": "Arun",
                "age": 120,
                "skill": "Python",
                "experience_level": "Beginner"
            },
            {
                "name": "Arun",
                "age": -5,
                "skill": "Java",
                "experience_level": "Beginner"
            }
        ]

        with self.assertRaises(ValueError):
            get_valid_data(responses)


if __name__ == "__main__":
    unittest.main()