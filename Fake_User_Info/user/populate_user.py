from user.models import *
from faker import Faker

fake = Faker()

def generate_user(n=15):
    
    for i in range(n):
        
        full_name = fake.name().split()
        first_name = full_name[0]
        last_name = full_name[1]
        user_email = fake.email()
        
        user = User.objects.create(first_name = first_name, last_name = last_name, user_email = user_email)
    