from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Amazon:
    
    def __init__(self):
        
        Service = ChromiumService(executable_path="chromedriver")
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory' : './'}# where the downloads should be 
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(service=Service,options=chrome_options)
        self.wait = WebDriverWait(self.driver,10)
        self.action = ActionChains(self.driver)
    
    def sort_items(self,sort_by):
        mp = {'recommend': 0,'Price L-H':1,'Price: H-L':2,'Rating':3}
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH,"//*[@id='search']//span[@class='a-dropdown-container']"))
        ).click()

        sort_by_list = self.wait.until(
            EC.visibility_of_all_elements_located((By.XPATH,"//div[@id='a-popover-2']//li"))
        )
        if(sort_by not in mp):
            print("invalid choice to sort items ")
            return 
        sort_by_list[mp[sort_by]].click()
    
    def apply_filter(self,ratings,price_range = (0,0)):
        
        rating_list = self.wait.until(
            EC.visibility_of_all_elements_located((By.XPATH,"//div[@id='reviewsRefinements']//li"))
        )
        rating_list[ratings - 4].click()
        # unable to do the sliders in amazon as there is no webelement which can be found  to move the sliders

    def search(self,search_item):
        
        self.driver.get('https://www.amazon.in')
        search_bar = self.wait.until(
            EC.visibility_of_element_located((By.XPATH,"//input[@id='twotabsearchtextbox']"))
        )
        search_bar.send_keys(search_item+Keys.ENTER)
    

    def get_data(self,no_of_pages = 2):
        items = []
        def scrape_data(prefix,product):
            
            link = (self.wait.until(
                EC.presence_of_element_located((By.XPATH,f'{prefix}//a'))
            ).get_attribute('href'))
            
            ratings = (self.wait.until(
                EC.presence_of_element_located((By.XPATH,f'{prefix}//span[@aria-label][1]'))
            ).get_attribute('aria-label'))

            ratedby = (self.wait.until(
                EC.presence_of_element_located((By.XPATH,f'{prefix}//span[@aria-label][2]'))
            ).get_attribute('aria-label'))

            detail_list = product.text.split('\n')
            
            name = detail_list[0]
            if(name == 'Sponsored'):
                name = detail_list[1]
            try:
                price = list(filter(lambda x: x.startswith("\u20B9"), detail_list))[0].split(" ")[0]
            except:
                price = 'currently unavailable'
            return [name,price,ratings,ratedby,'amazon',link]

        for page in range(no_of_pages):
            i = 1
            p_count = 0
            while(True):
                try:
                    product = self.wait.until(
                        EC.presence_of_element_located((By.XPATH,f"//div[@data-asin][{i}]"))
                    )
                except:
                    break
                if(product.get_attribute('data-asin') == ''):
                    i+=1
                    continue
                items.append(scrape_data(f'//div[@data-asin][{i}]',product))
                p_count+=1
                i+=1
            print(f'page {page+1} has {p_count} products')
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"))
            ).click()

        return items 
                



        




