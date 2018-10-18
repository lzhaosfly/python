from selenium import webdriver

stockChartsUrl = 'https://stockcharts.com/h-sc/ui'
browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get(stockChartsUrl)
