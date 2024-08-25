from selenium.webdriver.common.by import By

from pegeobject.objectdata import AddObject


class Test_Automation:
    Object=AddObject

    def test_CredCart(self, Setup):
        self.driver = Setup
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credencetest@test.com")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        if self.driver.title == 'CredKart':
            print("We pass first step")
            assert True

        else:
            print("It is Failed testcase")
            self.driver.save_screenshot("Screenshots\failed.png")

    def test_addObjectdata(self, Setup):
        self.driver = Setup
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credencetest@test.com")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.Object.playstation()
        self.Object.add_to_cart(self)
