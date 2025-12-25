from selenium.webdriver.common.by import By


class MainPageLocators:
    # FAQ section
    FAQ_SECTION = (By.CLASS_NAME, "Home_FourPart__1uthg")
    FAQ_QUESTIONS = (By.CLASS_NAME, "accordion__button")
    FAQ_ANSWERS = (By.CLASS_NAME, "accordion__panel")
    
    # Order buttons
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    
    # Logo
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")