from pom.login import Login
from tests.mixins.PaymentRequestTestObjectsMixin import PaymentRequestTestObjectsMixin


class TestPaymentRequestIntegrationTestCase(PaymentRequestTestObjectsMixin):

    def sign_in(self, page):
        login_pom = Login(page)
        dashboard = login_pom.submit(self.get_user()['email'], self.get_user()['password'])
        return dashboard.guests_payment_request()

    def test_payment_request_settings(self, page):
        payment_request_settings_form = self.get_payment_request_settings_form()
        payment_request_pom = self.sign_in(page)
        payment_request_pom.click_settings_button()

        # Fills and save payment request settings form
        payment_request_pom.fill_payment_request_settings_information(payment_request_settings_form)
        payment_request_pom.common_actions.save()

        # Back and again click on settings button
        payment_request_pom.common_actions.click_back_button()
        payment_request_pom.click_settings_button()

        # Verify if settings information is loaded on the UI
        payment_request_pom.assert_invoice_settings_fields(payment_request_settings_form)
