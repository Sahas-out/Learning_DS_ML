from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Flipkart:
    
    def __init__(self):

        Service = ChromiumService(executable_path="chromedriver")
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory' : './'}# where the downloads should be 
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(service=Service,options=chrome_options)
        self.wait = WebDriverWait(self.driver,10)
        self.action = ActionChains(self.driver)



    def search(self,search_item):
        self.driver.get('https://www.flipkart.com')
        try:
            WebDriverWait(self.driver,3).until(
                EC.element_to_be_clickable((By.XPATH,"//span[@class='_30XB9F']"))
            ).click()
        except:
            pass
        search_bar = self.wait.until(
            EC.visibility_of_element_located((By.XPATH,"//input[@class='Pke_EE']"))
        )
        search_bar.send_keys(search_item+Keys.ENTER)

    def sort_by(self,sort_by):
        if(sort_by == 'Rating'):
            print("there is no sort by rating option in flipkart")
            return 
        mp = {'recommend': 0,'Price L-H':2,'Price: H-L':3}
        sort_by_list = self.wait.until(
            EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='sHCOk2']//div"))
        )
        sort_by_list[mp[sort_by]].click()

    def apply_filter(self,rating=-1,price_range=(0,0)):
        if(rating != -1):
            ratings_list = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH,"//section[@class='-5qqlC _2OLUF3'][2]//div[@class='ewzVkT _3DvUAf']"))
            )
            ratings_list[4-rating].click()
            # to confirm rating button has been clicked 
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH,"//section[@class='-5qqlC _2OLUF3'][2]//div[@class='aGZXck']"))
            )
            #

        min_menu = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,"//section[@class='FR+9+z _2OLUF3']//div[@class='suthUA']"))
        ).text.split('\n')
        i = 1
        while (i<len(min_menu))and(int(min_menu[i])<=price_range[0]):
            i+=1
        min_option = i-1
        i = 0
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH,f"//section[@class='FR+9+z _2OLUF3']//div[@class='suthUA']//option[{min_option+1}]"))
        ).click()

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH,f"//section[@class='FR+9+z _2OLUF3']//div[@class='_08gQ9q aOfogh']"))
        ).click()
        
        max_menu = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,"//section[@class='FR+9+z _2OLUF3']//div[@class='tKgS7w']"))
        ).text.split('\n') 
        max_menu[-1] = int(max_menu[-2]) + 1
        while(i<len(max_menu))and(int(max_menu[i])<=price_range[1]):
            i+=1
        max_option = i-1
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH,f"//section[@class='FR+9+z _2OLUF3']//div[@class='tKgS7w']//option[{max_option+1}]"))
        ).click()
        
    def get_data(self):
        pass

