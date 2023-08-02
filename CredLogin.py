from selenium.webdriver.common.by import By


class Test_Credence_002:

    def test_CredKart_Login_008(self, setup):
        self.driver = setup
        # Go to Url
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@1234")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login TestCase is Passed")
            self.driver.close()
            assert True
        except:
            print("Login TestCase is Failed")
            self.driver.close()
            assert False



