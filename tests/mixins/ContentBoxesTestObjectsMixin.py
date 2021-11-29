from tests.mixins.TestObjectsMixin import TestObjectsMixin


class ContentBoxesTestObjectsMixin(TestObjectsMixin):

    @staticmethod
    def get_menu_cb_form(name='Test Menu CB', description='This is a Menu CB.', published=True):
        return {'name': name, 'description': description, 'published': published}

    @staticmethod
    def get_menu_cb_section_form(name='Test Menu Section', description='This is a Menu CB section.'):
        return {'name': name, 'description': description}

    @staticmethod
    def get_menu_cb_item_form(name='Test Menu Item', description='This is a Menu CB item.', price='1.00'):
        return {'name': name, 'description': description, 'price': price}
