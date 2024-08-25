from selenium.webdriver.common.by import By


class AddObject:

    def __init__(self, driver):
        self.driver = driver

    def playstation(self):
        self.driver.find_element(By.XPATH, "//body/div[@class='container']/div[2]/div[1]/div[1]/div[1]/a[1]/img[1]").click()

    def add_to_cart(self,add):
        self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").send_keys("add")


