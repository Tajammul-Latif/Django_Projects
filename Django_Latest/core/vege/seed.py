from faker import Faker
import random
from .models import *
from django.db.models import Sum

fake = Faker()

def seed_db(n=10) -> None:
    try:
        departments = Department.objects.all()
        subjects = Subject.objects.all()
        
        for i in range(n):
            department = departments[random.randint(0, len(departments) - 1)]
            student_id = f'STU-0{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )

            for subject in subjects:
                marks = random.randint(40, 90)
                SubjectMarks.objects.create(
                    student=student_obj,
                    subject=subject,
                    marks=marks
                )
    except Exception as e:
        print(e)


def generate_report_card():
    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('Student_Marks__marks')).order_by('-marks', '-student_age')
    i = 1
    
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )
        i = i + 1