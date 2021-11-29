from pom.dashboard import Dashboard


class Login:
    # inputs
    _EMAIL = 'xpath=//input[@name="email"]'
    _PASSWORD = 'xpath=//input[@name="password"]'

    # buttons
    _SUBMIT = 'xpath=//button[.="Log in"]'

    def __init__(self, page):
        self.page = page
        self.page.goto('https://chezpierre-dab64d6a.localtest.me:42227/login/')

    def submit(self, email: str, password: str):
        self.page.fill(self._EMAIL, email)
        self.page.fill(self._PASSWORD, password)
        self.page.click(self._SUBMIT)
        return Dashboard(self.page)
