def user_login(driver, user_email, user_pass):
    """
    Input user email and user password with submit
    :param driver: webdriver instance
    :param user_email: user email used to kog in
    :param user_pass: password used to log in
    :return: None
    """
    # enter email
    login_field_element = driver.find_element_by_xpath('//*[@name="email" and @class="form-control"]')
    login_field_element.send_keys(user_email)
    # enter password
    password_field_element = driver.find_element_by_xpath(
        '//*[@name="password" and @class="form-control js-child-focus js-visible-password"]')
    password_field_element.send_keys(user_pass)
    # click submit
    sign_in_button_element = driver.find_element_by_id('submit-login')
    sign_in_button_element.click()