from create_logging import create_logging
import platform
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import logging


chromeDriverPath: str = './driver/chromedriver_unix'
if platform.version() == 'Windows':
    chromeDriverPath = './driver/chromedriver_win32.exe'
elif platform.version() == 'Linux':
    chromeDriverPath = './driver/chromedriver_linux'

browser = webdriver.Chrome(executable_path=chromeDriverPath)


def stockChartsRun(symbol: str, page_load_time: int = 30, logging_level=logging.INFO):
    stock_logging = create_logging(level=logging_level)
    stockChartsUrl = 'https://stockcharts.com/h-sc/ui'
    browser.set_page_load_timeout(page_load_time)
    try:
        browser.get(stockChartsUrl)
    except TimeoutException:
        stock_logging.info(
            'page not finish load, but we will try to get things now...')

    # find symbol input
    symbolInputEl = browser.find_element_by_id('symbol')
    symbolInputEl.send_keys(symbol)

    # find button and click
    submitButtonEl = browser.find_element_by_id('submitButton')
    try:
        submitButtonEl.click()
    except TimeoutException:
        stock_logging.info(
            'search page not finish load, but will try to continue...')

    # set up EMA
    for i in range(3):
        EMASelectEl = Select(browser.find_element_by_id(f'overType_{i}'))
        EMASelectEl.select_by_value('EMA')
        EMAInputEl = browser.find_element_by_id(f'overArgs_{i}')
        EMAInputEl.clear()
        if i == 0:
            EMAInputEl.send_keys('3')
        elif i == 1:
            EMAInputEl.send_keys('13')
        else:
            EMAInputEl.send_keys('34')

    # set up char Attribute
    rangeSelectEl = Select(browser.find_element_by_id('dataRange'))
    rangeSelectEl.select_by_value('predef:0|1|0')

    chartTypeSelectEl = Select(browser.find_element_by_id('symStyle'))
    chartTypeSelectEl.select_by_visible_text('Solid Line')

    # reset the indicators part
    clearAllEl = browser.find_element_by_css_selector(
        '#section4Long > .workbench a')
    clearAllEl.click()
    browser.switch_to.alert.accept()

    stock_logging.info('.....finish..')


def main():
    stockChartsRun(symbol='IQ')


if __name__ == '__main__':
    main()
