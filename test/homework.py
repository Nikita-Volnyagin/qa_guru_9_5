from selene.support.shared import browser
from selene import have, be, command
import os


def test_registration_form_demo_qa():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type("Nikita")
    browser.element('#lastName').type("Nikitin")
    browser.element('#userEmail').type('test.test@test.com')
    browser.all('[for^=gender-radio]').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('7999158449')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="3"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1998"]').click()
    browser.element('.react-datepicker__day--020').click()
    browser.element('#subjectsInput').should(be.blank).type('arts').press_enter()
    browser.all('[for^=hobbies-checkbox-3]').element_by(have.exact_text('Music')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img/Image.jpg'))
    browser.element('#currentAddress').type('Russia, Samara, 446222')
    browser.element('.css-yk16xz-control').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').perform(command.js.click)

    browser.element('.table').all('td').even.should(have.exact_texts(
        'Nikita Nikitin',
        'test.test@test.com',
        'Male',
        '7999158449',
        '20 April,1998',
        'Arts',
        'Music',
        'Image.jpg',
        'Russia, Samara, 446222',
        'NCR Noida'))