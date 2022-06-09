from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button"
    email = 'pati.it.qa@gmail.com'

    def type_in_email(self, email, password):
        self.field_send_keys(self.login_field_xpath, email)
        self.field_send_keys(self.password_field_xpath, password)
        self.click_on_the_element(self.sign_in_button_xpath)