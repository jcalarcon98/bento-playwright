from pom.common_actions import CommonActions


class MenusCB:
    def __init__(self,  page):
        self.page = page
        self.common_actions = CommonActions(page)

    # input
    _NAME = 'xpath=//input[@id="menu-name"]'
    _DESCRIPTION = 'xpath=//section[.//label[text()="Description"]]//div[@contenteditable="true"]'
    _INSERT_IMAGE = 'xpath=//button[.="INSERT"]'
    _SECTION_NAME = 'xpath=//input[starts-with(@id,"section-name-")]'
    _ITEM_NAME = 'xpath=//input[contains(@id,"-item-name")]'
    _ITEM_PRICE = 'xpath=//input[starts-with(@id,"price-value-")]'

    # textarea
    _SECTION_DESCRIPTION = 'xpath=//textarea[starts-with(@id,"section-description-")]'
    _ITEM_DESCRIPTION = 'xpath=//textarea[contains(@id,"-item-description")]'

    # button
    _ADD_IMAGE = 'xpath=//i[.="add"]'
    _ADD_MENU_SECTION = '//button[.="Add Menu Section"]'
    _ADD_MENU_ITEM = '//button[contains(., "Add Menu Item")]'
    _DONE = 'xpath=//button[.="DONE"]'

    # image
    _DEFAULT_IMAGE = 'data-testid=image-gallery-image-0'

    # dropdown
    _LAYOUT = 'id=menu-layout-settings'

    @staticmethod
    def _get_section_query(section_name):
        return f'//h2[text()="{section_name}"]/ancestor::section'

    def change_name(self, name):
        self.page.click(self._NAME, **{'click_count': 3})
        self.page.type(self._NAME, name)

    def change_description(self, description):
        self.page.click(self._DESCRIPTION, **{'click_count': 3})
        self.page.type(self._DESCRIPTION, description)

    def change_layout(self, layout):
        self.page.select_option(self._LAYOUT, label=layout)

    def change_section_name(self, section_name):
        self.page.click(self._SECTION_NAME, **{'click_count': 3})
        self.page.type(self._SECTION_NAME, section_name)

    def change_section_description(self, section_description):
        self.page.click(self._SECTION_DESCRIPTION, **{'click_count': 3})
        self.page.type(self._SECTION_DESCRIPTION, section_description)

    def change_item_name(self, item_name):
        self.page.click(self._ITEM_NAME, **{'click_count': 3})
        self.page.type(self._ITEM_NAME, item_name)

    def change_item_description(self, item_description):
        self.page.click(self._ITEM_DESCRIPTION, **{'click_count': 3})
        self.page.type(self._ITEM_DESCRIPTION, item_description)

    def change_item_price(self, item_price):
        self.page.click(self._ITEM_PRICE, **{'click_count': 3})
        self.page.type(self._ITEM_PRICE, f'${item_price}')

    def click_add_menu_section(self, column_name: str):
        section_query = self._get_section_query(column_name)
        button_locator = f'xpath={section_query}{self._ADD_MENU_SECTION}'
        self.page.click(button_locator)

    def click_add_menu_item(self, section_name: str):
        menu_section_query = f'//h2[text()="{section_name}"]/../../../..'
        add_menu_item_locator = f'xpath={menu_section_query}{self._ADD_MENU_ITEM}'
        self.page.click(add_menu_item_locator)

    def add_image(self):
        self.page.click(self._ADD_IMAGE, **{'click_count': 2})
        self.page.click(self._DEFAULT_IMAGE)
        self.page.click(self._INSERT_IMAGE)

    def add_menu_section_to_column(self, column_name: str, menu_section_form):
        column_title_locator = f'xpath=//h2[.="{column_name}"]'

        self.click_add_menu_section(column_name)
        self.change_section_name(menu_section_form['name'])
        self.change_section_description(menu_section_form['description'])
        self.page.click(column_title_locator)

    def add_item_to_menu_section(self, section_name: str, menu_item_form):
        self.click_add_menu_item(section_name)
        self.change_item_name(menu_item_form['name'])
        self.change_item_description(menu_item_form['description'])
        self.change_item_price(menu_item_form['price'])
        self.page.click(self._DONE)

    def change_menu_item_order(self, source_menu_item_name, target_menu_item_name, menu_name, up=True):

        # Define selector needed
        source_menu_item_selector = f'//div[.="{source_menu_item_name}"]'
        target_menu_item_selector = f'//div[.="{target_menu_item_name}"]'
        menu_selector = f'//h2[.="{menu_name}"]/../../../following-sibling::div'
        source_menu_item_selector = f'xpath={menu_selector}{source_menu_item_selector}'
        source_menu_item_draggable_selector = f'{source_menu_item_selector}/../../../../../span'
        target_menu_item_selector = f'xpath={menu_selector}{target_menu_item_selector}/../../../../../..'

        # Define locators
        source_menu_item_locator = self.page.locator(source_menu_item_selector)
        source_menu_item_draggable_locator = self.page.locator(source_menu_item_draggable_selector)
        target_menu_item_locator = self.page.locator(target_menu_item_selector)

        # Drag and drop interaction
        destiny_bounding_box = target_menu_item_locator.bounding_box()
        # breakpoint()
        source_menu_item_locator.hover()
        source_menu_item_draggable_locator.hover()
        y_movement_amount = -(destiny_bounding_box['height']) if up else destiny_bounding_box['height']
        self.page.mouse.down()
        self.page.mouse.move(0, 0)
        self.page.mouse.move(0, y_movement_amount)
        self.page.mouse.up()
