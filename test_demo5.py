import time


from selenium.webdriver.common.by import By

class Test_case_login_param:

    def test_homepage_001(self, setup):
        self.driver = setup
        if self.driver.title == "CredKart":
            assert True
        else:
            assert False

    def test_login_002(self, getDataforlogin, setup):
        self.driver = setup
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(getDataforlogin[0])
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(getDataforlogin[1])
        self.driver.find_element(By.XPATH, "// button[ @ type = 'submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login Successfully with valid credential")
            self.driver.save_screenshot("E:\Software Testing Class Notes\Python\PytestFramework\Screenshot\\"+getDataforlogin[0]
                               +" "+getDataforlogin[1]+"test_cred_login001.PNG")
            self.driver.close()
            assert True
        except:
            print("Invalid credential")
            self.driver.save_screenshot("E:\Software Testing Class Notes\Python\PytestFramework\Screenshot" + getDataforlogin[0]
                               + " " + getDataforlogin[1] + "test_cred_login001.PNG")
            self.driver.close()
            assert False







