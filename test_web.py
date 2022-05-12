from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import unittest


username = "applesauce"
password = "password"

class DemoBlazeTest(unittest.TestCase):
    def setUp(self):
        #create a headless Chrome browser
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        self.driver = Chrome("chromedriver")


    def test1(self): #Create Sign up

        self.driver.get('https://www.demoblaze.com/index.html')
        main_page = self.driver.current_window_handle
        sleep(1)
        # get the login modele
        self.driver.find_element_by_xpath('//*[@id = "signin2"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id = "sign-username"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id = "sign-password"]').send_keys(password)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
        sleep(5)

    def test2(self): # Log in and password.

        self.driver.get('https://www.demoblaze.com/index.html')
        sleep(1)
        # get the login modele
        self.driver.find_element_by_xpath('//*[@id="login2"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginusername"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

    def test3(self): #Added 2 items in the shopping cart.Enter all the details in the page (First Name/ Last Name etc). Click on cancel
        name = 'bob'
        country = 'usa'
        city = 'sd'
        cc = '1234567890'
        month = '12'
        year ='12'

        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.find_element_by_xpath('//*[@id="login2"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginusername"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(password)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="tbodyid"]/div[2]/div/a').click()


        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Waiting for alert timed out')
            self.driver.switch_to.alert.accept()
            print
            "alert accepted"
        except TimeoutException:
            print
            "no alert"

        self.driver.find_element_by_xpath('//*[@id="navbarExample"]/ul/li[1]/a').click()
        sleep(10)
        self.driver.find_element_by_xpath('//*[@id="tbodyid"]/div[2]/div/div/h4/a').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="tbodyid"]/div[2]/div/a').click()

        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Waiting for alert timed out')
            self.driver.switch_to.alert.accept()
            print
            "alert accepted"
        except TimeoutException:
            print
            "no alert"

        self.driver.find_element_by_xpath('//*[@id="cartur"]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[2]/button').click()
        sleep(5)

        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="country"]').send_keys(country)
        self.driver.find_element_by_xpath('//*[@id="city"]').send_keys(city)
        self.driver.find_element_by_xpath('//*[@id="card"]').send_keys(cc)
        self.driver.find_element_by_xpath('//*[@id="month"]').send_keys(month)
        self.driver.find_element_by_xpath('//*[@id="year"]').send_keys(year)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="orderModal"]/div/div/div[3]/button[1]').click()

    def test4(self): #Delete 2 items from the shopping card, Log out
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.find_element_by_xpath('//*[@id="login2"]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="loginusername"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(password)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="cartur"]').click()
        sleep(10)
        self.driver.find_element_by_xpath('//*[@id="tbodyid"]/tr[1]/td[4]/a').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="tbodyid"]/tr/td[4]/a').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="logout2"]').click()
        sleep(5)

    def test5(self): #Log in again and password, How many items on the shopping cart?
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.find_element_by_xpath('//*[@id="login2"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginusername"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(password)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="cartur"]').click()
        sleep(5)
        cols= self.driver.find_elements_by_xpath('//*[@id="tbodyid"]/tr[1]/td')
        items_in_cart= (len(cols))
        return items_in_cart

    def test6(self): #Repeating test 2 - 4 Add 1/delete 1
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.find_element_by_xpath('//*[@id="login2"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginusername"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(password)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="tbodyid"]/div[2]/div/a').click()

        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Waiting for alert timed out')
            self.driver.switch_to.alert.accept()
            print
            "alert accepted"
        except TimeoutException:
            print
            "no alert"
        self.driver.find_element_by_xpath('//*[@id="cartur"]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="tbodyid"]/tr[1]/td[4]/a').click()
        sleep(5)

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
