from pom.login import Login
from tests.mixins.ContentBoxesTestObjectsMixin import ContentBoxesTestObjectsMixin


class TestMenusCBFujiIntegrationTestCase(ContentBoxesTestObjectsMixin):

    def sign_in(self, page):
        login_pom = Login(page)
        dashboard = login_pom.submit(self.get_user()['email'], self.get_user()['password'])
        return dashboard.content_boxes_menus()

    def test_add_menu_cb(self, page, browser):
        menu_cb_form = self.get_menu_cb_form()
        menu_section_form_one = self.get_menu_cb_section_form('Test Menu Section One')
        menu_section_form_two = self.get_menu_cb_section_form('Test Menu Section Two')
        menu_item_form = self.get_menu_cb_item_form()

        menus_cb_pom = self.sign_in(page)

        menus_cb_pom.common_actions.add()
        menus_cb_pom.change_name(menu_cb_form['name'])
        menus_cb_pom.change_description(menu_cb_form['description'])
        menus_cb_pom.add_image()

        menus_cb_pom.change_layout('Two Columns')

        # Create first menu section on UI
        menus_cb_pom.add_menu_section_to_column(column_name='Column One ', menu_section_form=menu_section_form_one)
        menus_cb_pom.add_item_to_menu_section(
            section_name=menu_section_form_one['name'], menu_item_form=menu_item_form
        )

        # Create second menu section on UI
        menus_cb_pom.add_menu_section_to_column(column_name='Column Two ', menu_section_form=menu_section_form_two)

        # Add 2 menu items on UI to second menu section
        menus_cb_pom.add_item_to_menu_section(
            section_name=menu_section_form_two['name'], menu_item_form=menu_item_form
        )
        menu_item_form_two = dict(menu_item_form)
        menu_item_form_two['name'] = 'Custom name'
        menus_cb_pom.add_item_to_menu_section(
            section_name=menu_section_form_two['name'], menu_item_form=menu_item_form_two
        )

        # Drag and drop interaction
        menus_cb_pom.change_menu_item_order(
            source_menu_item_name=menu_item_form_two['name'],
            target_menu_item_name=menu_item_form['name'],
            menu_name=menu_section_form_two['name']
        )

        menus_cb_pom.change_menu_item_order(
            source_menu_item_name=menu_item_form['name'],
            target_menu_item_name=menu_item_form_two['name'],
            menu_name=menu_section_form_two['name']
        )

        menus_cb_pom.common_actions.save()
        menus_cb_pom.common_actions.back()
