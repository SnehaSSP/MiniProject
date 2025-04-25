import pytest
from faker import Faker

fake = Faker()

@pytest.fixture(scope="module")
def get_data():
    firstname = fake.first_name()
    lastname = fake.last_name()
    email = fake.email()
    password = fake.password()
    yield firstname, lastname, email, password
