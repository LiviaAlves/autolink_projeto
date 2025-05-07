from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5173/register")  # ajuste se o path for diferente
        time.sleep(5)  # esperar o frontend carregar

    def test_registro_com_sucesso(self):
        driver = self.driver

        # Preencher os campos do formulário
        driver.find_element(By.NAME, "username").send_keys("usua_teste_selenium")
        driver.find_element(By.NAME, "email").send_keys("test_selnium@example.com")
        driver.find_element(By.NAME, "password").send_keys("sen_segura123")
        driver.find_element(By.NAME, "confirmPassword").send_keys("sen_segura123")
        
        # Clicar no botão de registro
        driver.find_element(By.CLASS_NAME, "register-submit-button").click()

        # Esperar resposta
        time.sleep(5)

        # Verifica se foi redirecionado para a dashboard (ajuste se necessário)
        self.assertIn("http://localhost:5173/login", driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
