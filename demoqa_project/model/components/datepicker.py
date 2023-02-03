from selene import have
from selene.support.shared import browser


def select_date(locator, value):
    browser.element(locator).all('option').element_by(have.exact_text(value)).click()
