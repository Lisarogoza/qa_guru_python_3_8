from demoqa_project.model.pages import practice_form


def test_form_filling():
    practice_form.open_page()

    practice_form.add_firstname('Olga')
    practice_form.add_lastname('Efimova')
    practice_form.add_email('Oefi_Lefi@yandex.ru')

    practice_form.select_gender('Female')

    practice_form.add_phone_number('9000000000')

    practice_form.select_date()
    practice_form.select_month('May')
    practice_form.select_year('1965')
    practice_form.select_day('17')

    practice_form.select_subject('English')

    practice_form.select_hobby('Music')

    practice_form.picture_upload()

    practice_form.add_address('Build, floor, flat')

    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')
    practice_form.click_submit()

    practice_form.assert_info(
        'Olga Efimova',
        'Oefi_Lefi@yandex.ru',
        'Female',
        '9000000000',
        '17 May,1965',
        'English',
        'Music',
        'snow_cat.png',
        'Build, floor, flat',
        'NCR Delhi'
    )

    practice_form.click_close_button()
