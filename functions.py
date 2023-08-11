from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Login(driver,login,password):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"user-name")))
        driver.find_element(By.ID,"user-name").send_keys(login)

        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"password")))
        driver.find_element(By.ID,"password").send_keys(password,Keys.ENTER)

    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")
    

def ReadFile():
    return pd.read_excel("Data.xlsx")


def SelectItem(driver,ItemName):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"item_4_title_link")))
        driver.execute_script("""
        function AddItemToCart(ItemName){
            for(count = 1; count <= 8; count++){
                CurrentItem = document.evaluate(`/html/body/div/div/div/div[2]/div/div/div/div[${count}]/div[2]/div[1]/a/div`,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue
                console.log(CurrentItem.innerText.includes(ItemName))
                if(CurrentItem.innerText.includes(ItemName)){
			        console.log("foi")
                    document.evaluate(`/html/body/div/div/div/div[2]/div/div/div/div[${count}]/div[2]/div[2]/button`,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.click();
                    break
                }
        
            }      
        }"""+f"AddItemToCart('{ItemName}')")
        print(ItemName)
        driver.execute_script(f"")


    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")
    

def BtnCheckout(driver):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"checkout")))
        driver.find_element(By.ID,"checkout").click()


    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")
       

def BtnContinue(driver):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"continue")))
        driver.find_element(By.ID,"continue").click()


    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")
       

def BtnFinish(driver):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"finish")))
        driver.find_element(By.ID,"finish").click()


    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")
       

def FillingOutForms(driver,Id,Value):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,Id)))
        driver.find_element(By.ID,Id).send_keys(Value)


    except Exception as error:
        raise Exception(f"Error: {str(error)}\n Line: {error.__traceback__.tb_lineno}")
       
    

