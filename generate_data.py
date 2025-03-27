import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'pnp.settings')
import django
django.setup()

from faker import Faker
from core.models import Place, CodeType, Code, Comment, Vote
from django.contrib.auth.models import User
import random
from model_bakery.recipe import Recipe

myfake = Faker()

# Function to create random latitude and longitude within DC area
def random_latitude():
    return round(random.uniform(38.5, 39.5), 6)

def random_longitude():
    return round(random.uniform(-77.5, -76.5), 6)

# Generate fake users for auth system
def create_fake_user():
    return User.objects.create_user(username=myfake.user_name(), password="password123")

# Create sample users
for _ in range(10):  # Create 10 fake users
    create_fake_user()

# Create fake Place entries
for _ in range(50):  # Create 50 places
    owner = random.choice(User.objects.all())
    place = Place(
        name=myfake.company(),
        lat=random_latitude(),
        long=random_longitude(),
        owner=owner
    )
    place.save()

# 2 code types: wifi passwords and door codes
code_types = [1,2]

lock_type = CodeType(name="Restroom Door Lock Code")
lock_type.save()

wifi_type = CodeType(name="Wifi Password")
wifi_type.save()


# Create some bathroom door lock codes
for _ in range(50):  
    code_type_id = 1
    place = random.choice(Place.objects.all())
    owner = random.choice(User.objects.all())
    code = Code(
        value=random.randint(1000, 9999),
        code_type_id=code_type_id,
        place=place,
        owner=owner
    )
    code.save()


# Create some wifi passwords
for _ in range(50):  
    code_type_id = 2
    place = random.choice(Place.objects.all())
    owner = random.choice(User.objects.all())
    code = Code(
        value=myfake.word(),
        code_type_id=code_type_id,
        place=place,
        owner=owner
    )
    code.save()


# Create some Votes - TODO: make this unique
for _ in range(200):
    code = random.choice(Code.objects.all())
    user = random.choice(User.objects.all())
    worked = random.choice([True, False])
    vote = Vote(
        user = user,
        code = code,
        worked = worked
    )
    vote.save()



# Create some Comments
for _ in range(50): 
    code = random.choice(Code.objects.all())
    owner = random.choice(User.objects.all())
    comment = Comment(
        text=myfake.text(),
        code=code,
        owner=owner
    )
    comment.save()

print("Sample data generated successfully!")