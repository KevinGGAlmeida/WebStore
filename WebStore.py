
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from functions import Login,ReadFile,SelectItem,BtnCheckout,FillingOutForms,BtnContinue, BtnFinish
import datetime

class WebStore:

    def __init__(self,Site,user,senha):
        self.Site = Site
        self.user = user
        self.senha = senha
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-dev-shm-usage')


    def Data(self):
        self.data = ReadFile()


    def Launch(self):
        self.driver = webdriver.Chrome(service=Service("/app/chromedriver"),options=self.chrome_options)
        self.driver.get(self.Site)


    def LoginWebStore(self):
        Login(self.driver,self.user,self.senha)


    def Checkout(self):
        for lines in self.data.index:
            self.driver.get("https://www.saucedemo.com/inventory.html")
            SelectItem(self.driver,str(self.data['Item'][lines]))
            self.driver.get("https://www.saucedemo.com/cart.html")
            BtnCheckout(self.driver)
            FillingOutForms(self.driver,'first-name',str(self.data['Name'][lines]).split(" ")[0])
            FillingOutForms(self.driver,'last-name',str(self.data['Name'][lines]).split(" ")[-1])
            FillingOutForms(self.driver,'postal-code',str(self.data['Zip'][lines]))
            BtnContinue(self.driver)
            BtnFinish(self.driver)
            print(f"Line: {lines}, Product: {str(self.data['Item'][lines])} Done")

        self.driver.save_screenshot("Finished.jpg")

print(datetime.datetime.now())
Run = WebStore('https://www.saucedemo.com/','standard_user','secret_sauce')
Run.Data()
Run.Launch()
Run.LoginWebStore()
Run.Checkout()
print(datetime.datetime.now())
