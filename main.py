from pydantic import BaseModel, Field, ValidationError


# 1. Define Student data structure
class Student(BaseModel):
    name: str
    age: int = Field(gt=0, le=100)
    skill: str
    experience_level: str


# 2. Validate AI responses with retry mechanism
def get_valid_data(responses):

    for attempt, response in enumerate(responses[:3], start=1):

        try:
            print(f"\nAttempt {attempt}")

            student = Student(**response)

            print("Valid data received!")
            return student

        except ValidationError as e:
            print("Invalid response!")
            print(e)

    raise ValueError("Failed after 3 attempts")