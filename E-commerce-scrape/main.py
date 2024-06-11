import pandas as pd
from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from AmazonSearch import Amazon
from FlipkartSearch import Flipkart
# filters that user can apply 
#price -range, customer ratings, website

# sort by user can apply 
#price low-high high-low , customer rating

# display table 
# product name , prize , customer rating , url 
columns = [
    'name',
    'price',
    'rating',
    'ratedby',
    'service',
    'link'
]
# amazon = Amazon()
flipkart = Flipkart()
search_item = 'Airdopes'
# amazon.search(search_item)
# amazon.sort_items('Rating')
# amazon.apply_filter(ratings=4)
# amazon_list = amazon.get_data(no_of_pages=2)
# amazon.driver.quit()
# df = pd.DataFrame(amazon_list,columns=columns)
# df.to_excel('items.xlsx')

flipkart.search(search_item)
# flipkart.sort_by('Price L-H')
# flipkart.apply_filter(rating = 3,price_range=(1000,3700))
