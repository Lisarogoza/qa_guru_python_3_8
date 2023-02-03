from selene.support.shared import browser
from selene import be, have
from demoqa_project.model.components import checkbox, dropdown, datepicker, radiobutton
from demoqa_project.utils import file_path, scroll


def open_page():
    browser.open('/automation-practice-form')


def add_firstname(firstname):
    browser.element('#firstName').should(be.blank).type(firstname)


def add_lastname(lastname):
    browser.element('#lastName').should(be.blank).type(lastname)


def add_email(email):
    browser.element('#userEmail').should(be.blank).type(email)


def select_gender(gender):
    radiobutton.radiobtn('[name=gender]', gender)


def add_phone_number(phone):
    browser.element('#userNumber').should(be.blank).type(phone)


def add_address(address):
    scroll.scroll_to('#city')
    browser.element('#currentAddress').should(be.blank).type(address)


def select_date():
    browser.element('#dateOfBirthInput').click()


def select_day(day):
    browser.element(f'.react-datepicker__day--0{day}').click()


def select_month(month):
    browser.element('.react-datepicker__month-select').click()
    datepicker.select_date('.react-datepicker__month-select', month)


def select_year(year):
    browser.element('.react-datepicker__year-select').click()
    datepicker.select_date('.react-datepicker__year-select', year)


def select_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


# def select_hobbie(hobbie):
def select_hobby(hobby):
    checkbox.hobby('[for^=hobbies-checkbox]', hobby)


#   browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobbie)).click()


def picture_upload():
    file_path.create_file_path('#uploadPicture', 'pictures\\snow_cat.png')


def select_state(state):
    dropdown.choose_option('#state', state)


def select_city(city):
    dropdown.choose_option('#city', city)


def click_submit():
    browser.element('#submit').press_enter()


def assert_info(*args):
    browser.element('.table').all('.table td:nth-child(2)').should(have.texts(args))


def click_close_button():
    scroll.scroll_to('#closeLargeModal')
    browser.element('#closeLargeModal').click()
