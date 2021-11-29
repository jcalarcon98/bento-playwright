from pom.common_actions import CommonActions


class PaymentRequests:

    def __init__(self, page):
        self.page = page
        self.common_actions = CommonActions(page)

    # input
    _FROM_NAME = 'xpath=//input[@name="from_name"]'
    _REPLY_TO_EMAIL = 'xpath=//input[@name="reply_to_email"]'

    # button
    _SETTINGS_BUTTON = 'data-testid=settings'

    def click_settings_button(self):
        self.page.click(self._SETTINGS_BUTTON)

    def fill_payment_request_settings_information(self, payment_request_settings_form: dict):
        self.page.click(self._FROM_NAME, **{'click_count': 3})
        self.page.type(self._FROM_NAME, payment_request_settings_form['from_name'])
        self.page.click(self._REPLY_TO_EMAIL, **{'click_count': 3})
        self.page.type(self._REPLY_TO_EMAIL, payment_request_settings_form['reply_to_email'])

    def assert_invoice_settings_fields(self, payment_request_settings_form: dict):
        from_name_value = self.page.input_value(self._FROM_NAME)
        reply_to_email_value = self.page.input_value(self._REPLY_TO_EMAIL)
        assert from_name_value == payment_request_settings_form['from_name']
        assert reply_to_email_value == payment_request_settings_form['reply_to_email']
