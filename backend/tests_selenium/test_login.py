from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5173/login")

    def test_login_com_sucesso(self):
        driver = self.driver
        driver.find_element(By.NAME, "username").send_keys("usuario_teste")
        driver.find_element(By.NAME, "password").send_keys("senha_teste")
        driver.find_element(By.CLASS_NAME, "login-submit-button").click()

        time.sleep(2)
        self.assertIn("http://localhost:5173", driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()