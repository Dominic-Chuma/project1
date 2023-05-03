import pytest
import time as sl
from Pages.page1 import Page1
from TestData.page_data1 import BASE_URL, LOCATE_HEADER, HEADER_BY, HEADER_TEXT

#Create object from page class


# Tests for the UI POMs in the pages file
class TestCases_forPage1:

    # def __init__(self) -> None:
    #     pass
    
    def test_urls1(self):
        page1 = Page1()
        assert page1.get_site_url(BASE_URL) == True
        assert page1.get_site_url("https://cozy-profiterole-618935") == False
        sl.sleep(2)

        
    def test_title(self):
        page1 = Page1()
        assert page1.page_title("Game Catalogue") == True
        assert page1.page_title("Game Catal") == False
        sl.sleep(2)

    
    def test_header_text(self):
        page1 = Page1()
        assert page1.page_heading(HEADER_BY, LOCATE_HEADER) == HEADER_TEXT
        page1.close_browser()
        sl.sleep(2)



# page1.close_browser()
