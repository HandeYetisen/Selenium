# Yeni testlerimiz için bu linki kullanacağız https://www.saucedemo.com/ 

# Bu site özel olarak selenium test için üretilmiş. Ödevlerimizi bu sitenin tüm testlerini yapacak şekilde şekillendireceğiz

# Her bir ister bir pytest fonksiyonu olacak şekilde yazılmalıdır.
# Bu ödev için isterler:

# -Doğru bilgilerden standard_user kullanıcı adıyla giriş yapılmanın doğru olup olmadığı kontrol edilmelidir.
# -Yanlış bilgiler girildiğinde uyarı çıkıp çıkmadığı test edilmelidir.
# -Yanlış bilgiler girildiğinde çıkan uyarı mesajının doğruluğu kontrol edilmelidir Epic sadface: Username and password do not match any user in this service
# -Ana sayfada 6 adet ürün listelendiği kontrol edilmelidir.
# -Sepete Ekle butonuna tıklandığında butonun texti REMOVE olmalıdır.
# -Sepete 1 adet ürün eklendiğinde sağ üstteki sepet üzerinden 1 sayısı çıkmalıdır.



from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import date
from pathlib import Path
from constants import *

class Test_Saucedemo:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
       
    def teardown_method(self):
        self.driver.quit()

#ister-1-Doğru bilgilerden standard_user kullanıcı adıyla 
#giriş yapılmanın doğru olup olmadığı kontrol edilmelidir.

    def test_login_succesful(self):
        self.driver.get(BASE_DOMAIN_URL)
    
        userNameBoxXPath = USER_NAME_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,userNameBoxXPath)))
        userNameBox = self.driver.find_element(By.XPATH,userNameBoxXPath)
        userNameBox.send_keys("standard_user")
        
        passwordBoxXPath = PASSWORD_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,passwordBoxXPath)))
        passwordBox = self.driver.find_element(By.XPATH,passwordBoxXPath)
        passwordBox.send_keys("secret_sauce")

        loginBtnXPath = LOGIN_BTN_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,loginBtnXPath)))
        loginBtn = self.driver.find_element(By.XPATH,loginBtnXPath)
        loginBtn.click()
              
        title = self.driver.title
        assert title == "Swag Labs"
        
      
# #ister-2-Yanlış bilgiler girildiğinde uyarı çıkıp çıkmadığı test edilmelidir.


    def test_login_error(self):
       
        self.driver.get(BASE_DOMAIN_URL)
    
        userNameBoxXPath = USER_NAME_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,userNameBoxXPath)))
        userNameBox = self.driver.find_element(By.XPATH,userNameBoxXPath)
        userNameBox.send_keys("stndrd_user")
        
        passwordBoxXPath = PASSWORD_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,passwordBoxXPath)))
        passwordBox = self.driver.find_element(By.XPATH,passwordBoxXPath)
        passwordBox.send_keys("secret")

        loginBtnXPath = LOGIN_BTN_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,loginBtnXPath)))
        loginBtn = self.driver.find_element(By.XPATH,loginBtnXPath)
        loginBtn.click()

        error_message_xpath = ERROR_MESSAGE_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,error_message_xpath)))
        error_message = self.driver.find_elements(By.XPATH,error_message_xpath)
        error_message_size = len(error_message)

        assert error_message_size > 0

      

# #ister-3-Yanlış bilgiler girildiğinde çıkan uyarı mesajının doğruluğu kontrol edilmelidir 
# #Epic sadface: Username and password do not match any user in this service

    def test_login_error_message(self):
        self.driver.get(BASE_DOMAIN_URL)

        userNameBoxXPath = USER_NAME_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,userNameBoxXPath)))
        userNameBox = self.driver.find_element(By.XPATH,userNameBoxXPath)
        userNameBox.send_keys("stndrd_user")
        
        passwordBoxXPath = PASSWORD_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,passwordBoxXPath)))
        passwordBox = self.driver.find_element(By.XPATH,passwordBoxXPath)
        passwordBox.send_keys("secret")

        loginBtnXPath = LOGIN_BTN_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,loginBtnXPath)))
        loginBtn = self.driver.find_element(By.XPATH,loginBtnXPath)
        loginBtn.click()

        error_message_fail_Xpath = ERROR_MESSAGE_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, error_message_fail_Xpath)))
        error_Message_fail= self.driver.find_element(By.XPATH,error_message_fail_Xpath)
        error_Message_fail_text = error_Message_fail.text
        assert error_Message_fail_text == "Epic sadface: Username and password do not match any user in this service"


        
#ister4-Ana sayfada 6 adet ürün listelendiği kontrol edilmelidir.        


    def test_product_count(self):
        self.driver.get(BASE_DOMAIN_URL)
    
        userNameBoxXPath = USER_NAME_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,userNameBoxXPath)))
        userNameBox = self.driver.find_element(By.XPATH,userNameBoxXPath)
        userNameBox.send_keys("standard_user")
        
        passwordBoxXPath = PASSWORD_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,passwordBoxXPath)))
        passwordBox = self.driver.find_element(By.XPATH,passwordBoxXPath)
        passwordBox.send_keys("secret_sauce")

        loginBtnXPath = LOGIN_BTN_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,loginBtnXPath)))
        loginBtn = self.driver.find_element(By.XPATH,loginBtnXPath)
        loginBtn.click()

        product_count_class_name = PRODUCT_COUNT_CLASS_NAME
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,product_count_class_name)))
        productCount = self.driver.find_elements(By.XPATH,product_count_class_name)
        assert len(productCount)== 6
        

#ClassName = inventory_item_description
#ister5-Sepete Ekle butonuna tıklandığında butonun texti REMOVE olmalıdır.

    def test_basket_remove(self):
        self.driver.get(BASE_DOMAIN_URL)
    
        userNameBoxXPath = USER_NAME_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,userNameBoxXPath)))
        userNameBox = self.driver.find_element(By.XPATH,userNameBoxXPath)
        userNameBox.send_keys("standard_user")
        
        passwordBoxXPath = PASSWORD_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,passwordBoxXPath)))
        passwordBox = self.driver.find_element(By.XPATH,passwordBoxXPath)
        passwordBox.send_keys("secret_sauce")

        loginBtnXPath = LOGIN_BTN_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,loginBtnXPath)))
        loginBtn = self.driver.find_element(By.XPATH,loginBtnXPath)
        loginBtn.click()

        add_to_cart_xpath = ADD_TO_CART_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,add_to_cart_xpath)))
        addToCartBtn = self.driver.find_element(By.XPATH,add_to_cart_xpath)
        addToCartBtn.click()

        remove_btn_xpath = REMOVE_BTN
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,remove_btn_xpath)))
        removeBtn = self.driver.find_element(By.XPATH,remove_btn_xpath)
        removeBtn_text = removeBtn.text
        assert removeBtn_text == "REMOVE"
        



#ister6-Sepete 1 adet ürün eklendiğinde sağ üstteki sepet üzerinden 1 sayısı çıkmalıdır.

    def test_basket_number(self):
        self.driver.get(BASE_DOMAIN_URL)
    
        userNameBoxXPath = USER_NAME_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,userNameBoxXPath)))
        userNameBox = self.driver.find_element(By.XPATH,userNameBoxXPath)
        userNameBox.send_keys("standard_user")
        
        passwordBoxXPath = PASSWORD_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,passwordBoxXPath)))
        passwordBox = self.driver.find_element(By.XPATH,passwordBoxXPath)
        passwordBox.send_keys("secret_sauce")

        loginBtnXPath = LOGIN_BTN_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,loginBtnXPath)))
        loginBtn = self.driver.find_element(By.XPATH,loginBtnXPath)
        loginBtn.click()

        add_to_cart_xpath = ADD_TO_CART_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,add_to_cart_xpath)))
        addToCartBtn = self.driver.find_element(By.XPATH,add_to_cart_xpath)
        addToCartBtn.click()

        basket_count_xpath = BASKET_COUNT_XPATH
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,basket_count_xpath)))
        basketCount = self.driver.find_elements(By.XPATH,basket_count_xpath)
        
        assert len(basketCount) == 1
        


    


