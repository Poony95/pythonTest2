from selenium import webdriver
try:
    browser = webdriver.Chrome()
    browser.get("https://www.naver.com")
except ConnectionRefusedError:
    print ( '서버에 연결할 수 없습니다.')
    