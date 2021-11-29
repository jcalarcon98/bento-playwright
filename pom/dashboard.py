from pom.menus_cb import MenusCB
from pom.payment_requests import PaymentRequests


class Dashboard:
    _SIDE_GUESTS_PAYMENT_REQUESTS = 'data-testid=sidebar-nav-link-guest-invoices'
    _SIDE_CONTENT_BOXES = 'xpath=//span[.="Content Boxes"]/../following-sibling::i'
    _SIDE_CONTENT_BOXES_MENU = 'data-testid=sidebar-nav-link-website-contentboxes-menus'

    def __init__(self, page):
        self.page = page

    def guests_payment_request(self):
        self.page.click(self._SIDE_GUESTS_PAYMENT_REQUESTS)
        return PaymentRequests(self.page)

    def content_boxes_menus(self):
        self.page.click(self._SIDE_CONTENT_BOXES)
        self.page.click(self._SIDE_CONTENT_BOXES_MENU)
        return MenusCB(self.page)
