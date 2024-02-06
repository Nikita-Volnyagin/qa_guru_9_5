import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_gender: str
    user_phone_number: str
    month: str
    year: str
    day: str
    user_subject: str
    user_hobby: str
    user_picture: str
    user_current_address: str
    user_state: str
    user_city: str


test_user = User(
    first_name='Nikita',
    last_name='Nikitin',
    user_email='test.test@test.com',
    user_gender='Male',
    user_phone_number='7999158449',
    month='April',
    year='1998',
    day='20',
    user_subject='Economics',
    user_hobby='Sports',
    user_picture='Image.jpg',
    user_current_address='Russia, Samara, 446222',
    user_state='NCR',
    user_city='Noida',
)