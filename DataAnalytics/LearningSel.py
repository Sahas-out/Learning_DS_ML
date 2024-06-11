from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
import time
import pandas as pd

# class_names = [ 
#  'styles__ElementHeading-ahs9zc-5 haxmIv' #'name' 
# , 'styles__ElementTypeLabel-ahs9zc-4 BFSeu' #'position' 
# , 'styles__Club-ahs9zc-6 cvAaWL' #'team' 
# ]
c_name = 'styles__StatValue-sc-1tsp201-2 fgGEXH'
url = "https://fantasy.premierleague.com/statistics"

Service = ChromiumService(executable_path="chromedriver")
driver = webdriver.Chrome(service=Service)
driver.get(url)
columns = ['name','pos','team','inj','prc','form',
           'pts','st','mp','gs','a','xG',
           'xA','xGI','CS','GC','xGC','OG',
           'PS','PM','YC','RC','S','BP',
           'BPS','I','C','T','II']
#  now clicking on accept the cookies buttosn
acpt_cookies = driver.find_element(By.ID,'onetrust-accept-btn-handler')
acpt_cookies.click()
time.sleep(0.5)
# //*[@id="root"]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/button Now finding the info buttons of players 
xpath = '//*[@id="root"]/div[2]/div/div[1]/table/tbody/tr/td[2]/button'
buttons = driver.find_elements(By.XPATH,xpath)
time.sleep(1)
stats =[]
for i in range(len(buttons)):#len(buttons)):
    buttons[i].click()
    player_stats=[]
    # time.sleep(1)
    print(i)
    player_stats.append(driver.find_element(By.XPATH,'//h2[@class="styles__ElementHeading-ahs9zc-5 haxmIv"]').text)
    player_stats.append(driver.find_element(By.XPATH,'//span[@class="styles__ElementTypeLabel-ahs9zc-4 BFSeu"]').text)
    player_stats.append(driver.find_element(By.XPATH,'//div[@class="styles__Club-ahs9zc-6 cvAaWL"]').text)
    try:
        inj = driver.find_element(By.XPATH,'//div[@type="news"]').text
        try:
            player_stats.append(inj[inj.index('%')-2:inj.index('%')+1])
        except:
            player_stats.append('0%')
    except:
        player_stats.append('100%')
    
    lst = driver.find_elements(By.XPATH,'//div[@class="styles__StatValue-sc-1tsp201-2 fgGEXH"]')
    player_stats.append(lst[0].text)
    player_stats.append(lst[1].text)
    player_stats.append(lst[4].text)
    

    
    path = '//*[@id="root-dialog"]/div/dialog/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tfoot/tr[1]/td'
    for x in range(4,26):
        player_stats.append(driver.find_element(By.XPATH,f'{path}[{str(x)}]').text)
    stats.append(player_stats)
    driver.find_element(By.XPATH,'//*[@id="root-dialog"]/div/dialog/div/div[1]/div/button').click()
    # time.sleep(1)
driver.quit()
df = pd.DataFrame(stats,columns = columns)
df.to_excel('fb.xlsx')


# //*[@id="root-dialog"]/h2[@class="styles__ElementHeading-ahs9zc-5 haxmIv"]