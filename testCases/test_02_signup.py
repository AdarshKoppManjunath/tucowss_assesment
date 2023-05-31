import pytest
from pages.home_page import HomePage
from pages.signup_page import SignUp

@pytest.mark.usefixtures("setup")
class Test_02_SignUp:
    home_page_url="https://www.aircanada.com/"

    def test_home_page_title(self):
        self.driver.get(self.home_page_url)
        actual_title=self.driver.title
        assert actual_title=="Air Canada" , "AirCanada Web Application is not loaded."
            
    #login page direct link is keep redirecting to homepage for me. So navigating to login from homepage
    #Verify that a new user can successfully sign up with valid credentials
    def test_signup_positive(self):
       home_page_obj=HomePage(self.driver,self.util_obj)
       home_page_obj.naviagte_to_create_account_page()
       self.driver.maximize_window()
       signin_page_obj=SignUp(self.driver,self.util_obj,"test_signup_positive")
       signin_page_obj.input_email()
       signin_page_obj.input_password()
       signin_page_obj.check_box()
       signin_page_obj.continue_button()
       signin_page_obj.input_firstname()
       signin_page_obj.input_lastname()
       signin_page_obj.input_gender()
       signin_page_obj.input_birth_date()
       
    #Verify that an error message is displayed when attempting to log in with invalid credentials.
    def test_signup_negative(self):
       home_page_obj=HomePage(self.driver,self.util_obj)
       home_page_obj.naviagte_to_create_account_page()
       self.driver.maximize_window()
       signin_page_obj=SignUp(self.driver,self.util_obj,"test_signup_negative")
       signin_page_obj.input_email()
       signin_page_obj.input_password()
       signin_page_obj.check_box()
       signin_page_obj.continue_button()
       if not self.driver.find_element('xpath',"//span[contains(text(),'This email is already associated with an Aeroplan account')]"):
           assert False, "Account Should Not be created with already registered email."