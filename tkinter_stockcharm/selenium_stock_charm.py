import platform
import logging
from create_logging import create_logging
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


def driverInit(driver_logging=create_logging()):
    chromeDriverPath: str = './driver/chromedriver_unix'

    if platform.system() == 'Windows':
        chromeDriverPath = './driver/chromedriver_win32.exe'
    elif platform.system() == 'Linux':
        chromeDriverPath = './driver/chromedriver_linux'

    driver = webdriver.Chrome(executable_path=chromeDriverPath)

    initialUrl = 'https://www.google.com'

    try:
        driver.get(initialUrl)
    except TimeoutException:
        driver_logging.info(
            'try to open google...')

    return driver


def stockChartsRun(symbol: str, driver: webdriver, page_load_time: int = 10, stock_logging=create_logging()):

    driver.execute_script("window.open('https://stockcharts.com/h-sc/ui');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(page_load_time)

    # find symbol input
    symbolInputEl = driver.find_element_by_id('symbol')
    symbolInputEl.send_keys(symbol)

    # find button and click
    submitButtonEl = driver.find_element_by_id('submitButton')
    try:
        submitButtonEl.click()
    except TimeoutException:
        stock_logging.info(
            'search page not finish load, but will try to continue...')

    # set up EMA
    for i in range(3):
        EMASelectEl = Select(driver.find_element_by_id(f'overType_{i}'))
        EMASelectEl.select_by_value('EMA')
        EMAInputEl = driver.find_element_by_id(f'overArgs_{i}')
        EMAInputEl.clear()
        if i == 0:
            EMAInputEl.send_keys('3')
        elif i == 1:
            EMAInputEl.send_keys('13')
        else:
            EMAInputEl.send_keys('34')

    # set up char Attribute
    rangeSelectEl = Select(driver.find_element_by_id('dataRange'))
    rangeSelectEl.select_by_value('predef:0|1|0')

    chartTypeSelectEl = Select(driver.find_element_by_id('symStyle'))
    chartTypeSelectEl.select_by_visible_text('Solid Line')

    # reset the indicators part
    clearAllEl = driver.find_element_by_css_selector(
        '#section4Long > .workbench a')
    clearAllEl.click()
    driver.switch_to.alert.accept()

    stock_logging.info('.....finish..')


def main():
    driverTest = driverInit()
    stockChartsRun(symbol='IQ', driver=driverTest, page_load_time=10)


if __name__ == '__main__':
    main()
