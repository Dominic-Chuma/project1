# To use time
import time as sl


from Pages.base_page import  EC, WebDriverWait, chrome_driver, BASE_URL

class Page1:

    def __init__(self) -> None:
        # pass
        chrome_driver.get(BASE_URL)
        sl.sleep(3)
    
    def get_site_url(self,url):
        wait = WebDriverWait(chrome_driver, 10, 1, "False")
    
        try:
            wait.until(EC.url_to_be(url))
            return True
        except:
            return False

    def page_title(self, title):
        wait = WebDriverWait(chrome_driver, 10, 1)
        try:
            wait.until(EC.title_is(title))
            return True
        except:
            return False
        # if wait.until(EC.title_is(title)):
        #     return True
        
    
    def page_heading(self, locator1, locator2):
        wait = WebDriverWait(chrome_driver, 10, 1)
        try:
            # wait.until(EC.text_to_be_present_in_element_value(locator,text))
            find_text = chrome_driver.find_element(locator1, locator2).text
            return find_text
        except:
            return False
        

    # Close browser....
    def close_browser(self):
        chrome_driver.quit()
