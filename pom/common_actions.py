class CommonActions:

    def __init__(self, page):
        self.page = page

    # button
    _ADD_NEW = 'data-testid=add-new'
    _SAVE_BUTTON = 'data-testid=save'
    _BACK_BUTTON = 'data-testid=back'
    _MODAL_CONFIRM_BUTTON = 'data-testid=modal-confirm'

    # alert
    _FLOATING_SAVE_SUCCESS_ALERT = 'data-testid=alert-success'
    _FLOATING_SAVE_DANGER_ALERT = 'data-testid=alert-danger'

    def add(self):
        self.page.click(self._ADD_NEW)

    def save(self, fail_expected=False):
        if fail_expected:
            self.page.click(self._SAVE_BUTTON)  # floating alert appears
            alert_message = self.page.inner_text(self._FLOATING_SAVE_DANGER_ALERT)
            self.click_floating_danger_alert()  # floating alert disappears
        else:
            self.page.click(self._SAVE_BUTTON)  # floating alert appears
            alert_message = self.page.inner_text(self._FLOATING_SAVE_SUCCESS_ALERT)
            self.click_floating_success_alert()  # floating alert disappears

        return alert_message

    def back(self, unsaved=False):
        if unsaved:
            self.page.click(self._BACK_BUTTON)
            self.page.click(self._MODAL_CONFIRM_BUTTON)
        else:
            self.page.click(self._BACK_BUTTON)

    def click_floating_danger_alert(self):
        self.page.click(self._FLOATING_SAVE_DANGER_ALERT)

    def click_floating_success_alert(self):
        self.page.click(self._FLOATING_SAVE_SUCCESS_ALERT)

    def click_back_button(self):
        self.page.click(self._BACK_BUTTON)
