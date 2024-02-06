from demoqa_tests.pages.registration_page import RegistrationPage

def test_practice_from():
    registration_page = RegistrationPage()
    registration_page.open_registration_page()

    registration_page.fill_first_name('Nikita')
    registration_page.fill_last_name('Nikitin')
    registration_page.fill_user_email('test.test@test.com')
    registration_page.gender_selection('Male')
    registration_page.fill_user_phone_number(7999158449)
    registration_page.fill_date_of_birth('1998', 'April', '20')
    registration_page.select_user_subject('Economics')
    registration_page.user_hobby_checkbox('Sports')
    registration_page.user_picture('Image.jpg')
    registration_page.user_current_adress('Russia, Samara, 446222')
    registration_page.user_state('NCR')
    registration_page.user_city('Noida')
    registration_page.submit_the_form()

    registration_page.should_registered_user_with(
        'Nikita Nikitin',
        'test.test@test.com',
        'Male',
        '7999158449',
        '20 April,1998',
        'Economics',
        'Sports',
        'Image.jpg',
        'Russia, Samara, 446222',
        'NCR Noida',
    )