# Selenium

## 1. simple usage

```python
browser = webdriver.Chrome(executable_path='./chromedriver')

url = 'https://yoururl.com'
browser.set_page_load_timeout(5) # this is the page load time. Default = 30

try:
    browser.get(url)
except TimeoutException:
    browser.execute_script("window.stop();") # if time out, we don't want window continue to load
    logging.info(
        'page not finish load, but we will try to get things now...')

# input element
inputEl = browser.find_element_by_id('symbol')
inputEl.clear()
inputEl.send_keys('what you want to input')

submitButtonEl = browser.find_element_by_id('submitButton') # form submit button, page will reload, so we need to try the button click incase time out
try:
    submitButtonEl.click()
except TimeoutException:
    logging.info(
        'search page not finish load, but will try to continue...')

# selec element
selectEl = Select(browser.find_element_by_id(f'overType_1'))
selectEl.select_by_value('EMA')

# a link button
clearAllEl = browser.find_element_by_css_selector(
    '#section4Long > .workbench a')
clearAllEl.click()

# if window shows an confimation dialog, then accept will just click ok
browser.switch_to.alert.accept()
```

Note:

-   You need to download the corresponding driver first.
-   Better to give a time out value.
-   use `find_element_by_*` to get a webpage element
-   `inputElement.sendKey(value)` can set the value to your input. You may want to clean the input first. Then using `inputEl.clear()`
-   `button.click()` can trigger a button click. But be careful about if the click will load web page. Then you need to try/catch the timeout error.
-   Select element can use `selectEl = Select(browser.find_element_by_id(f'overType_1'))` to get. Then you have `selectEl.select_by_*` to select a dropdown value.
-   `browser.switch_to.alert.accept()` or `browser.switch_to.alert.dismiss()` to accept or dismiss window confirm dialog.