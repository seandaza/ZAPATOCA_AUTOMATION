import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAutomation(unittest.TestCase):

    def setUp(self):
        #Inicializando Chrome
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/95.0.4638.54 Safari/537.36")
        self.driver = webdriver.Chrome('web_automation_testing\chromedriver.exe', chrome_options=opts) 
        self.driver.maximize_window()
        #driver = webdriver.Remote('http://selenium:4444/wd/hub', DesiredCapabilities.CHROME)
        #Identificando el url de la pagina 
        url = "https://staging-zapatoca.miaguila.com/registro/?hidecaptcha=true"
        #Abriendo la pagina
        self.driver.get(url)
        time.sleep(1)

    def test_automation_CU1(self):
        # Registro de usuario y Login
        indices = [0,1,2,4,5,6,7,8]

        payload = {
            "0": "Jhean",
            "1": "Daza",
            "2": "Herrera",
            "4": "1126428239",
            "5": "seandaza@gmail.com",
            "6": "3167951589",
            "7": "Hola123",
            "8": "Hola123"
        }

        for elm in indices:
            textBox = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/div/div[3]/div[2]/div/div[1+"'+str(elm)+'"]/div[1]/input')
            textBox.send_keys(payload[str(elm)])
            time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 800);")
        time.sleep(1)
        aceptar_politicas = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[4]/div/div[3]/div[2]/div/label/input')
        aceptar_politicas.click()


        crear_cuenta = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[4]/div/div[3]/div[2]/div/button')
        crear_cuenta.click()

        Alert(self.driver).accept()

        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)
    
        ciudad = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/form/div[2]/div[2]/div/div/input')
        ciudad.send_keys("Bogotá")
        ciudad.send_keys(Keys.ARROW_DOWN)
        boton_ciudad = self.driver.find_element_by_xpath('//*[@id="autocomplete-item-0"]')
        boton_ciudad.click()

        carrera = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/form/div[2]/div[3]/div[1]/div/div/select')
        carrera.send_keys("Carrera")

        numero_carrera = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/form/div[2]/div[3]/div[2]/div/div[1]/input')
        numero_carrera.send_keys("104")

        numero_carrera1 = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/form/div[2]/div[4]/div[1]/div/div[1]/input')
        numero_carrera1.send_keys("# 152a")

        numero_carrera2 = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/form/div[2]/div[4]/div[2]/div/div[1]/input')
        numero_carrera2.send_keys("-55")

        iniciar_sesion = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/form/div[2]/div[5]/p/span/a')
        iniciar_sesion.click()
        time.sleep(3)

        textBox1 = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[4]/div/div[3]/div[2]/div[1]/div[1]/div[1]/input')
        textBox1.send_keys(payload["5"])

        textBox2 = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[4]/div/div[3]/div[2]/div[1]/div[2]/div[1]/input')
        textBox2.send_keys(payload["7"])

        boton_ingresar = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[4]/div/div[3]/div[2]/div[1]/button')
        boton_ingresar.click()
        time. sleep(2)

        cerrar_mensaje = self.driver.find_element_by_css_selector('#__layout > div > div.relative.lg\:mt-36 > div.delivery-panel > div.overlay-delivery-panel.max-w-full.bottom > div.header > svg > path')
        cerrar_mensaje.click()
        time.sleep(3)

        # Agregar productos al carrito
        categorias = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/span')
        categorias.click()
        time.sleep(2)

        descuento = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[3]/div[3]/div/div/ul/li[1]/div/a')
        time.sleep(3)
        descuento.click()
        time.sleep(5)

        boton_limpiar = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/button[1]')
        time.sleep(3)
        boton_limpiar.click()
        time.sleep(2)


        for i in range(5):
            products = self.driver.find_elements_by_xpath('//a[@class="product block"]')
            print("Total productos: ",len(products))  # Debuging
            print("productos: ", products)            # Debuging
            time.sleep(3)
            products[i].click()
            time.sleep(3)                          
            agregar = self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[4]/div[3]/div/div[2]/div[4]/button')
            agregar.click()
            time.sleep(3)
            
            try:
                casa = self.driver.find_element_by_xpath('//h3[@class="location-name"]')
                casa.click()
                time.sleep(3)
            except:
                pass
            
            try:
                cerrar = self.driver.find_element_by_css_selector('#__layout > div > div.panel.is-open > div.cart-container > header > button')
                time.sleep(1)
                cerrar.click()
            except:
                pass
            time.sleep(2)            
            self.driver.back()
            time.sleep(3)       
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()  