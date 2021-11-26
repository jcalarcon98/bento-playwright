import pytest
import unittest

from playwright.sync_api import Page


class DragAndDropIntegrationTestCase(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_drag_and_drop(self):
        self.page.goto("https://letcode.in/dropable")

        src_elem = self.page.query_selector("id=draggable") 
        dest_elem = self.page.query_selector("id=droppable")

        if (src_elem and dest_elem):
            srcBound = src_elem.bounding_box()
            dstBound = dest_elem.bounding_box()

            print(srcBound)

            if (srcBound and dstBound) :
                self.page.mouse.move(srcBound['x'] + srcBound['width'] / 2, srcBound['y'] + srcBound['height'] / 2)
                self.page.mouse.down()
                self.page.mouse.move(dstBound['x'] + dstBound['width'] / 2, dstBound['y'] + dstBound['height'] / 2)
                self.page.mouse.down()

    # https://playwright.dev/python/docs/api/class-mouse/