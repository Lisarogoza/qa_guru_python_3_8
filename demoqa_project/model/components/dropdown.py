from selene import have
from selene.support.shared import browser


def choose_option(locator, text):
    browser.element(locator).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(text)).click()
