from tests.mixins.TestObjectsMixin import TestObjectsMixin


class PaymentRequestTestObjectsMixin(TestObjectsMixin):

    @staticmethod
    def get_payment_request_settings_form(from_name='Test from name', reply_to_email='testreply@getbento.com'):
        return {'from_name': from_name, 'reply_to_email': reply_to_email}
