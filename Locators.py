from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGO_IMAGE =          (By.CLASS_NAME,'log-img')
    LOGIN_DE_TXT =        (By.CLASS_NAME,'.login-text.wow.bounceInDown')
    USERNAME =            (By.XPATH,"//input[contains(@class,'ui-inputfield') and contains(@type,'text')]")
    PASSWORD =            (By.XPATH,"//input[contains(@class,'ui-inputfield') and contains(@type,'password')]")
    LOGIN_BTN=            (By.CLASS_NAME,"login-button")
    ERROR_USERNAME =      (By.XPATH,"//form[contains(@class,'ng-untouched')]/div[1]/div/label")
    ERROR_PASSWORD =      (By.XPATH,"//form[contains(@class,'ng-untouched')]/div[2]/div/label")
    ERROR_USER_PASS =     (By.CSS_SELECTOR,".ui-g-12 p")




class ForgetPasswordLocator(object):
    FORGET_PASSWORD =     (By.XPATH,"//p[@class='login-text']")
    FGT_PASSWORD_FIELD =  (By.XPATH,"//input[contains(@class,'ui-inputfield') and contains(@type,'text')]")
    FGT_PASSWORD_BTN =    (By.CLASS_NAME,"login-button")
    FGT_PASSWORD_EMAIL_ERROR = (By.XPATH,"//div[@class='login-inner']/div/label")





